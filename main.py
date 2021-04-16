import requests
import pandas as pd
from utils import *

def findchronopost(lat,lng,cp,commune):
  headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.chronopost.fr/expeditionAvanceeSec/ounoustrouver.html',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

  params = (
        ('lat', str(lat)),
        ('lon', str(lng)),
        ('r', '140'),
        ('z', str(cp)),
        ('c', str(commune)),
        ('a', ''),
        ('p', 'FR'),
        ('lang', 'null'),
    )


  response = requests.get('https://www.chronopost.fr/expeditionAvanceeSec/stubpointsearch.json', headers=headers, params=params)
  data = response.json()
  relais=pd.DataFrame(r for r in data['olgiPointList'])
  for c in relais.select_dtypes(include=object).columns:
    relais[c]=relais[c].astype(str)
  return relais
  
def process(data, context):
  name=parse_parameters(data)
  cp,lat,lng,commune=name.split('|')
  relais = findchronopost(lat,lng,cp,commune)  
  sendresultstobq(relais,'mondialrelay','chronopost') 
