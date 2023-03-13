import re
import string
import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
import json
import ipbase


# PROGRAMAS DE APRENDIZAJE DE TUTORIALES Y CODEWARS II

# ******JSON
'''
data = """{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
  "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
    }
  }"""

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"] ["hide"])
'''

'''
input = """[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  },
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]"""

info = json.loads(input)
print('User count:', len(info))
for item in info:
  print('Name:', item['name'])
  print('Id:', item['id'])
  print('Attribute:', item['x'])
'''

# Te pide una dirección ip, la valida, la envía a la API de IpBase y te muestra el nombre del dominio y su ubicación

def checkIp(ip):
  numbers = ip.split('.')
  if (len(numbers) != 4):
    return None
  else:
    for n in numbers:
      if (n.isnumeric() == False) or (int(n) > 255):
        return None 
  return ip

IPBASE_URL = 'https://api.ipbase.com/v2/info?apikey='
IPBASE_KEY = 'pGuN4g48jM9NqmfI0PjUA3BSMziWMOtiaUS4dWHV'
ip_address = None

while True:
  
  while ip_address == None:
    ip_address = checkIp(input('Enter ip Address:'))
    if ip_address == None: print('Wrong IP Adress')
  
  url = ''.join(IPBASE_URL+IPBASE_KEY+'&ip='+ip_address)
  print('Retrieving', url)
  connection = urllib.request.urlopen(url)
  data = connection.read().decode()
  js = json.loads(data)
  #print(json.dumps(js, indent=4))
  print('Connection:', js['data']['connection']['organization'])
  print('Location:', js['data']['location']['city']['name_translated'],','
        , js['data']['location']['region']['name_translated'],','
        , js['data']['location']['continent']['name_translated'],'.')
  print('Coordinates: ', js['data']['location']['latitude'], ',', js['data']['location']['longitude'])
  break



       





