import re
import string
import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
import json
import ipbase
import sqlite3
from random import randint
import os

'''

# PROGRAMAS DE APRENDIZAJE DE TUTORIALES Y CODEWARS III

#SQLite

# Lee el archivo y añade a la base de datos los emails que hay y cuantos de cada uno

conn = sqlite3.connect("email.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

fname = input("Enter file name: ")
if (len(fname) < 1 ) : fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
  if not line.startswith("From: ") : continue
  pieces = line.split()
  email = pieces[1]
  cur.execute("SELECT Count FROM Counts WHERE email = ? ", (email,))
  row = cur.fetchone()
  if row is None:
    cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
  else:
    cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))
  conn.commit()



# https://www.sqlite.org/lang_select,html

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
  print(f"{row[0]}, {row[1]}")

cur.close()
'''


'''
# Hangman

from hangman_words import word_list
import hangman_art

os.system("cls")
length = len(word_list)
chosen_word = word_list[randint(0, length)]
display = []
for letter in chosen_word:
  display.append("_")

guess = None
end_of_game = False
lives = 6


while end_of_game == False:
  while (guess == None) or (len(guess) != 1) or (guess.isalpha() == False):
    print(hangman_art.logo)
    print("\n")
    print("".join(display))
    print("\n")
    print(hangman_art.stages[lives])
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    

  letter_position = 0
  letter_guessed = False
  

  for letter in chosen_word:
    if letter == guess:
      display[letter_position] = letter
      letter_guessed = True
    letter_position += 1
  guess = None
  
  if letter_guessed == False : lives -= 1
  

  
  if display.count('_') == 0:
    end_of_game = True
    print("You Win")
  elif lives == 0:
    end_of_game = True
    print(f"You lose, the secret word was: {chosen_word}")
'''
'''
# Calcular botes de pintura

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
  print(f"You will need {math.ceil((height * width) / cover)} cans of paint")
  
paint_calc(height=test_h, width= test_w, cover=coverage)
'''
'''
# Numero primo?  

n = int(input("Check this number: "))
def prime_checker(number):
  prime = True
  for n in range(2, number):
    if (number % n == 0):
      prime = False
  if prime is False : print("This number is not prime")
  else : print("This number is prime")   
  
  
prime_checker(number=n)
'''

'''
# Caesar Cipher

import math

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f'
          , 'g', 'h', 'i', 'j', 'k', 'l'
          , 'm', 'n', 'o', 'p', 'q', 'r'
          , 's', 't', 'u', 'v', 'w', 'x'
          , 'y', 'z', 'a', 'b', 'c', 'd'
          , 'e', 'f', 'g', 'h', 'i', 'j'
          , 'k', 'l', 'm', 'n', 'o', 'p'
          , 'q', 'r', 's', 't', 'u', 'v'
          , 'w', 'x', 'y', 'z'
          ]

print(logo)
print("\n")
should_continue = "y"

def caesar(text, shift, direction):
  new_text = ""
  new_index = None
  while shift > 26:
    shift -= 26
  if direction == "decode":
    shift *= -1  
  for letter in (text):
    if letter.isalpha() == False:
      new_text += letter
    else:
      new_index = alphabet.index(letter) + shift
      new_text += alphabet[new_index]
  print(f"The {direction}d text is: {new_text}")

while should_continue == "y":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  should_continue = input("Do you want to try it again? (y/n) ")

'''

'''
# Student grades

student_scores = {
  "Harry" : 81,
  "Ron" : 78,
  "Hermione" : 99,
  "Draco" : 74,
  "Neville" : 62,
}

student_grades = {}

for name in student_scores:
  if int(student_scores[name]) in range(91, 101) : student_grades[name] = "outstanding"
  elif int(student_scores[name]) in range(81, 91) : student_grades[name] = "Exceeds Expectations"
  elif int(student_scores[name]) in range(71, 81) : student_grades[name] = "Acceptable"
  elif int(student_scores[name]) < 70 : student_grades[name] = "Fail"

print(student_grades)
'''

'''
# Dictionaries and Lists

travel_log2 = {
  "France" : {
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits" : 12
    },
  "Germany" : {
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits" : 5
    },
}

travel_log = [
  {
    "country" : "France",
    "cities" : ["Paris", "Lille", "Dijon"],
    "visits" : 12
  },
  {
    "country" : "Germany", 
    "cities" : ["Berlin", "Hamburg", "Stuttgart"], 
    "visits" : 5
  },
]

def add_new_country(country, visits, cities) :
  travel_log.append({
    "country" : country,
    "cities" : cities,
    "visits" : visits
  }) 
  

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
'''

'''
# Blind Auction

from auction_art import logo



should_continue = "yes"
buyer = {}
buyer_list = []
high = 0
winner = 0

while should_continue == "yes" or should_continue == "y":
  os.system("cls")
  print(logo)
  name = input("What is your name? ")
  bid = input("What\'s your bid? ")
  buyer = {"Name" : name, "Bid" : bid}
  buyer_list.append(buyer)
  should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
  
"""
Manera más sencilla:
bids = {}
  
name = input("What is your name? ")
price = input("What is your bid? ")
bids[name] = price  
  
"""
  
for n in range(0, len(buyer_list)):
  h = int(buyer_list[n]["Bid"].strip("$"))
  if h > high:
    high = h
    winner = n
    
winner_name =  buyer_list[winner]["Name"]
winner_bid = buyer_list[winner]["Bid"]

os.system("cls")
print(logo)
print(f"\nThe winner is {winner_name} with {winner_bid}")  
'''
'''
# Calculator
 
from calculator_art import logo

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

should_continue = "yes"


def calculate(n1, n2, operation):
  return operations[operation](n1, n2)

def print_logo():
  os.system("cls")
  print(logo)
  print("\n")

print_logo()
num1 = float(input("What\'s the first number? "))
while should_continue == "yes":
  num2 = float(input("What\'s the second number? "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the line above ")
  answer = calculate(num1, num2, operation_symbol)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  should_continue = input(f"Do you want to continue calculating with this result? ({answer}) Type \'yes\', \'no\' or \'new\' ")
  num1 = answer
  if should_continue == "new":
    print_logo()
    num1 = float(input("What\'s the first number? "))
    should_continue = "yes"
  elif should_continue == "yes":
    print_logo()
'''


  












