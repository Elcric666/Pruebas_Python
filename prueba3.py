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

# Hangman

from hangman_words import word_list
import hangman_art


length = len(word_list)
chosen_word = word_list[randint(0, length)]
display = []
for letter in chosen_word:
  display.append("_")

guess = None
end_of_game = False
lives = 6

print(hangman_art.logo)
print("\n")
print("".join(display))

while end_of_game == False:
  while (guess == None) or (len(guess) != 1) or (guess.isalpha() == False):
    print("\n")
    guess = input("Guess a letter: ").lower()

  letter_position = 0
  letter_guessed = False
  

  for letter in chosen_word:
    if letter == guess:
      display[letter_position] = letter
      letter_guessed = True
    letter_position += 1
  guess = None
  print("".join(display))
  
  if letter_guessed == False : lives -= 1
  
  print(hangman_art.stages[lives])

  
  if display.count('_') == 0:
    end_of_game = True
    print("You Win")
  elif lives == 0:
    end_of_game = True
    print(f"You lose, the secret word was: {chosen_word}")
  










