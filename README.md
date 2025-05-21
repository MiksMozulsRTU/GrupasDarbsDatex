Miks Mozuls 3. grupa, Oskars Fisenkovs 4. grupa
 
## Uzdevuma apraksts

Izveidot programmu, kas automātiski nolasa visus interneta vietnē dateks, esošos portatīvo datoru piedāvājumus, un izvada šo informāciju excel tabulā.
Mēs izvēlējamies dateks.lv, jo saitnei ir saprotama HTML struktūra, kura labi strādā ar mūsu izvēlētājām bibliotēkām. Kā arī pieejami vairāki lēti, bet pietiekami jaudīgi portatīvie datori ikdienas vai biroja izmantošaanai.

## Nepieciešamās bibliotēkas

- openpyxl: Izmantots, lai izveidotu un kodu izmantojot modificētu excel tabulu
- bs4(BeautifulSoup): Izmantots, lai viegli pārmeklētu iegūtos HTML tekstus un no tiem iegūtu vajedzīgo informāciju
- requests: Izmantots, lai veiktu http pieprasījumus vietnei, lai saņemtu HTML tekstus, ko izmantojām
- time: Izmantots, lai palēlinātu pieprasījumu daudzumus, kuras sūtam saitnei

## Programmas lietošana 

Programmu palaižot tiks izvadīta informācija par to ka programmas darbība ir sākusies, programmas darbības laikā tā izvadīs tās saitnes kuras apskata. 
Programma paziņos darbības beigas un tiks izveidots excel fails. Programmas darbibās laikā jāparliecinās, ka nav atvērts excel dokuments, jo tas var radīt kļūdu.
