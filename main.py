import requests
import pandas as pd
from utils import *

def findchronopost(lat,lng,cp,commune):
  params = (
      ('lat', str(lat)),
      ('lon', str(lng)),
      ('r', '809'),
      ('z', str(cp)),
      ('c', str(commune)),
      ('a', ''),
      ('p', 'FR'),
      ('lang', 'null'),
  )
  response = requests.get('http://www.chronopost.fr/expeditionAvancee/stubpointsearchinterparservice.json', params=params,verify=False)
  data = response.json()
  relais=pd.DataFrame(r for r in data['olgiPointList'])
  for c in relais.select_dtypes(include=object).columns:
    relais[c]=relais[c].astype(str)
  sendresultstobq(relais,'mondialrelay','chronopost') 
  
def process(data, context):
  name=parse_parameters(data)
  cp,lat,lng,commune=name.split('|')
  findchronopost(lat,lng,cp,commune)  