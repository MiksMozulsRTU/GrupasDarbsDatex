## Uzdevuma apraksts

Izveidot programmu, kas automātiski nolasa visus interneta vietnē dateks, esošos portatīvo datoru piedāvājumus, un izvada šo informāciju excel tabulā. 

## Nepieciešamās bibliotēkas
- openpyxl: Izmantots, lai izveidotu un kodu izmantojot modificētu excel tabulu. 
- bs4(BeautifulSoup): Izmantots, lai viegli pārmeklētu iegūtos HTML tekstus un no tiem iegūtu vajedzīgo informāciju
- requests: Izmantots, lai veiktu http pieprasījumus vietnei, lai saņemtu HTML tekstus, ko izmantojām

## Programmas lietošana 

Programmu palaižot tiks izvadīta informācija par to ka programmas darbība ir sākusies, programmas darbības laikā tā izvadīs tās saitnes kuras apskata. Programma paziņos darbības beigas un tiks izveidots excel fails. Programmas darbibās laikā jāparliecinās, ka nav atvērts excel dokuments jo tas var radīt kļūdu
