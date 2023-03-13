import re
import string
import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET


# PROGRAMAS DE APRENDIZAJE DE TUTORIALES Y CODEWARS

'''
# ******Pide un número de horas y un precio por hora para imprimir el total. 
hours = 0
rate = 0

def comprobar_float(valor, mensaje):
  while valor is 0:
    try:
      valor = float(input(mensaje))
    except:
      print('Please enter a valid number')
  return valor
  
hours = comprobar_float(hours, 'Enter hours\n')
rate = comprobar_float(rate, 'Enter rate\n')
print('Pay: ' , hours * rate)
'''

'''
# ******Pide un nombre de archivo para abrirlo e imprimirte la cantidad de lineas que comienzan con 'The'
count = 0

fhand = None

while fhand == None:
  try:
    fname = input('Enter file name: ')
    fhand = open(fname)
  except:
    print('File name does not exist\n')
    
for line in fhand:
  line = line.rstrip()
  if not line.startswith('The '):
    continue
  print(line)
  count += 1
print(count)
'''


'''
# ******Te imprime una lista cambiando la primera letra por mayuscula

todo_list = [
  'shower',
  'brush teeth',
  'mow lawn',
  'eat brains',
]

for i, thing in enumerate(todo_list):
  print(i, thing.title())
'''


'''
# ******Te abre un archivo y te busca la palabra que esté dos palabras a la derecha de la palabra 'As'

fhand  = open('texto.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startswith('As'):
    continue
  words = line.split()
  print(words[2].title())
'''


'''
# ******Te dice cuantas veces se repite cada palabra en una lista

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] += 1

print(counts)
'''
# Lo mismo de otra manera
'''
for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)
'''

'''
# ******Cuenta la cantidad de cada palabra en el texto
fhand = open('texto.txt')
words = list()
counts = dict()

for lines in fhand:
  line = lines.lower()
  for word in line.split():
    counts[word] = counts.get(word, 0) + 1 

print(counts)

# Dice que palabras se repiten más veces
bigWord = list()
bigWords = list()

bigCount = None

for word, count in counts.items():
  if bigCount == None or count > bigCount:
    bigWord = word
    bigCount = count
  if (bigWord != word) and (count == bigCount):
    bigWord = bigWord + ':' + word
    
print(bigWord + ':' + str(bigCount))
'''

'''
# ******Ordena el diccionario en orden inverso

d = {'c': 84, 'a': 10, 'q': 54, 's': 67, 'u': 73, 'd': 20, 'e': 31, 'f': 47, 'g': 11, 'h': 59, 'i': 98, 'j': 92, 'k': 81, 'l': 29, 'm': 19, 'n': 65, 'o': 34, 'p': 40, 'r': 75}

temp = list()

for k, v in d.items():
  temp.append((v, k))
print(sorted(temp, reverse = True) , "\n")

# Otra manera mas sencilla
print( sorted([(v, k)for k, v in d.items()], reverse = True))
'''

'''
# ******Regular expressions

fhand = open('texto.txt')
for line in fhand:
  line = line.rstrip()
  if line.find('peaceful') >= 0:
    print(line)
'''
    
# Con RegEx
'''
fhand = open('texto.txt')
for line in fhand:
  line = line.rstrip()
  if re.search('^After', line):
    print(line)
'''
'''
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+' , x)
print(y)
y = re.findall('[MAEIOU]+' , x)
print(y)
'''
'''
x = 'From: Using the : character'
#y = re.findall('^F.+:' , x)
# ? -> non greedy
y = re.findall('^F.+?:' , x)
print(y)
'''
'''
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:15 2008'
y = re.findall('\S+@\S+' , x)
print(y)
y =  re.findall('^From (\S+@\S+)' , x)
print(y)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
'''
'''
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:15 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
'''

'''
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:15 2008'
print(line)
words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
print(pieces[1])

# Lo mismo con RegEx
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:15 2008'
y = re.findall('@(\S+)' , line)
print(y)
y = re.findall('@([^ ]*)' , line)
print(y)
y = re.findall('^From .*@([^ ]*)' , line)
print(y)
'''

'''
# ******Cambia cada primera letra de cada palabra de una cadena a mayuscula
 
string = 'This is a string'
words = string.split()
output = str()
for word in words:
  output = output + ' ' + word.capitalize()
print(output)
'''


'''
# ******Lee una cadena e imprime la cadena cambiando las letras lor valores numericos correspondientes a=1, b=2...

i = 1
diccio = dict()
text = 'The sunset sets at twelve o\'clock.'
output = str()

for letra in 'abcdefghijklmnopqrstuvwxyz':
  diccio[letra] = i
  i += 1
print(diccio)

for word in text.split():
  for letter in word:
    try:output = output + str(diccio[letter.lower()]) + ' '
    except:continue
output = output.rstrip()

print(output)

# manera pro
print(' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()))
'''
'''
list = ('8 3 -5 42 -1 0 0 -9 4 7 4 -4')
low = None
high = None
for n in list.split():
  if (low == None) or (int(n) < int(low)):
    low = n
  if (high == None) or (int(n) > int(high)):
    high = n
   
print(str(high) + ' ' + str(low))

# Manera pro
nn = [int(s) for s in list.split(" ")]
print("%i %i" % (max(nn),min(nn)))
'''

'''
# ******Comprueba que un pin sea de 4 O 6 digitos y que todos sean numeros

pin = '2572'

print((len(pin) == 4 or len(pin) == 6) and (pin.isdigit()))
# Manera pro
print(len(pin) in (4, 6) and pin.isdigit())
'''

'''
# ******Formatea una cadena de numeros en formato telefonico: (123) 456-7890

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'(%i%i%i) %i%i%i-%i%i%i%i' % tuple(n[i] for i in range(10)))

# Manera pro
print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))
'''

'''
# ******Recibe un numero, separa sus digitos, eleva cada uno al cuadrado los une y los presenta

number =  811181
output = ''
number_list = [int(n)**2 for n in str(number)]
for sqn in number_list:
  output = output + str(sqn)
print(int(output))

print(int(''.join(str(int(n)**2) for n in str(number))))
'''

'''
# ******Suma dos números y los presenta en binario

n1 = 8
n2 = 4
print(bin(n1 + n2).removeprefix('0b'))
# Mejor
print(bin(n1 + n2)[2:])
# Otra
print('{0:b}'.format(n1 + n2))
'''
'''
# ******Very simple web browser. Descarga un archivo de una dirección.

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print(data.decode())
mysock.close()
'''

# Otra manera más sencilla usando urllib
'''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())
'''
'''
# ******Scrapping con BeautifulSoup
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
  print(tag.get('href' , None))
'''
'''
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Abro la dirección y la "limpio"
url = 'http://www.dr-chuck.com/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
  print(tag.get('href', None))
'''

# Suma todos los numeros que hay entre a y b incluidos. Si es el mismo numero, devolver cualquiera de los dos
'''
a = 0
b = -1
if b < a:
  a,b = b,a
output = 0
if a == b:
  print(a)
else:
  for n in range(a,b + 1):
    output += n
  print(output)

# Manera pro
a = -1
b = -1
print(sum(range(min(a,b), max(a,b) + 1)))
'''

'''
# Resta los elementos del array2 al array1
array1 = [1,2,2,2,3]
array2 = [2,3]

for n in array2:
  while array1.count(n):
    array1.remove(n)
print(array1)

# Modo pro
array1 = [1,2,2,2,3]
array2 = [2,3]

print([n for n in array1 if n not in array2])
'''

# ******XML y XMS
'''

data = """<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
'''
'''
input = """<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>"""

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
  print('Name', item.find('name').text)
  print('Id', item.find('id').text)
  print('Attribute', item.get("x")) 
'''
   








  



