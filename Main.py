import requests 
from bs4 import BeautifulSoup  
from openpyxl import Workbook
from time import sleep



WEBSITE = "https://www.dateks.lv"

print("Start")

html = requests.get(WEBSITE+"/cenas/portativie-datori")
soup = BeautifulSoup(html.text) 
prod_array = soup.find_all("div",{'class':'prod'})




# Pārveido cenu float vērtībās izmantošanai excel
def GetPrice(x):     
    x = x.replace(" €", "") 
    x = x.replace(",",".")  
    x = x.replace(u"\xa0","")
    
    price = float(x)
    return price
    
# Iegūst visas lapas
links = soup.find("div",{'class':'pages'}).find_all('a')


# Iegūst katras lapas produktus.
for link in links: 
    print(f"{WEBSITE}{link.attrs['href']}") 
    new_html = requests.get(f"{WEBSITE}{link.attrs['href']}")
    loop_soup = BeautifulSoup(new_html.text)
    prod_array.extend(loop_soup.find_all("div",{'class':'prod'}))
    sleep(0.5)

wb = Workbook() 
ws = wb.active 
counter = 1 


# Izvada tabulas galveni
ws.append(["Nr","Nosaukums","Operētāj sistēma", "Cena","Komponentes", "Saite"])

# No katra produkta iegūst un izvada informāciju excel. 
for x in prod_array:
    split_text = x.find("div",{'class':'name'}).text.split(",") 
    price = x.find("div",{'class':'price'})
    links = x.find("a")    
    specs = x.find_all("div",{'class':'fv'})
    output = ""
    for string in specs:
        output += string.text + ":"

    output_price = "" 
    # Nepievienojot šo append metode nestrādā
    output_price = GetPrice(price.text)



    ws.append([counter,split_text[0],split_text[-1],output_price,output, WEBSITE+links.attrs['href']])
    
    
    counter += 1

print("done")
wb.save("output.xlsx") 
wb.close() 