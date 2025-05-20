import requests 
from bs4 import BeautifulSoup  
from openpyxl import Workbook
from time import sleep



class ProductMangaer: 
    WEBSITE = "https://www.dateks.lv"
    def __init__(self): 
        self.products = []
        self.raw_product = [] 
        self.links = [] 

    def populate_links(self):
        html = requests.get(self.WEBSITE+"/cenas/portativie-datori")
        soup = BeautifulSoup(html.text,features="lxml") 
        self.links = soup.find("div",{'class':'pages'}).find_all('a')

    def populate_raw_products(self): 
        self.populate_links() 

        for link in self.links: 
            print(f"{self.WEBSITE}{link.attrs['href']}") 
            new_html = requests.get(f"{self.WEBSITE}{link.attrs['href']}")
            loop_soup = BeautifulSoup(new_html.text,features="lxml")
            self.raw_product.extend(loop_soup.find_all("div",{'class':'prod'}))
            sleep(0.5)

    def get_price(self, price_text):     
        price_text = price_text.replace(" €", "") 
        price_text = price_text.replace(",",".")  
        price_text = price_text.replace(u"\xa0","")
        
        price = float(price_text)
        return price
    
    
    def build_product_list(self): 
        self.populate_raw_products() 
        for prod in self.raw_product: 
            split_text = prod.find("div",{'class':'name'}).text.split(",") 
            price = prod.find("div",{'class':'price'})
            link = prod.find("a")    
            specs = prod.find_all("div",{'class':'fv'})
            output = ""
            for string in specs:
                output += string.text + ":"

            output_price = "" 
            output_price = self.get_price(price.text) 

            self.products.append(Product(split_text[0],split_text[-1],output_price,output, self.WEBSITE+link.attrs['href']))


class Product: 
    
    def __init__(self, name, os ,price, specs, link): 
        self.name = name
        self.os = os 
        self.price = price
        self.specs = specs 
        self.link = link
    


def Main():

    print("Start")

    wb = Workbook() 
    ws = wb.active 
    counter = 1 

    # Izvada tabulas galveni
    ws.append(["Nr","Nosaukums","Operētāj sistēma", "Cena","Komponentes", "Saite"])
    manager = ProductMangaer() 
    manager.build_product_list() 

    # No katra produkta iegūst un izvada informāciju excel. 
    for x in manager.products:    
        ws.append([counter,x.name,x.os,x.price,x.specs,x.link])
        counter += 1

    print("done")
    wb.save("output.xlsx") 
    wb.close()  

Main()
