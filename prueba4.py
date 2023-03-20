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
import random
import os

'''
# Blackjack

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
  return deck[randint(0, 12)]

player_cards = []
house_cards = []
should_continue = True

player_cards.append(draw_card())
player_cards.append(draw_card())
if sum(player_cards) == 22 : player_cards[0] = 1

house_cards.append(draw_card())
house_cards.append(draw_card())
if sum(house_cards) == 22 : house_cards[1] = 1

os.system("cls")

while should_continue == True:
  os.system("cls")
  print("House\'s cards --->", end = " ")
  print(f"{house_cards[0]} X")
  print("Player\'s cards --> ", end = " ")
  for card in player_cards : print(f"{card} ", end = " ")
  print("\n")
  if (input("Do you want another card? (\'y\' \'n\') ")) == "y":
    player_cards.append(draw_card())
    if sum(player_cards) > 21:
      if 11 in player_cards:
        player_cards[player_cards.index(11)] = 1
      else:
        should_continue = False
        os.system("cls")
        print("You lose! ")  
  else:
    should_continue = False
    if sum(house_cards) < 17:
      house_cards.append(draw_card())
    if sum(house_cards) > 21:
      if 11 in house_cards:
        house_cards[house_cards.index(11)] = 1
    if (sum(house_cards) > 21) or (sum(house_cards) < sum(player_cards)):
      os.system("cls")
      print("You win! ")
    elif sum(house_cards) > sum(player_cards):
      os.system("cls")
      print("You lose! ")
    elif sum(house_cards) == sum(player_cards):
      os.system("cls")
      print("Draw! ")


print("House\'s cards --> ", end = " ")
for card in house_cards : print(f"{card} ", end = " ")
print("\n")
print("Player\'s cards --> ", end = " ")
for card in player_cards : print(f"{card} ", end = " ")
'''

'''
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from number_guessing import logo

secret_number = randint(1, 100)
should_continue = True
lives = 5

os.system("cls")
print("\n\n")
print(logo)
difficulty = input("At what difficulty do you want to play? \'hard\' \'easy\' ")
if difficulty == "hard" : lives = 5
elif difficulty == "easy" : lives = 10



def compare_numbers(secret_number, player_guess):
  if secret_number == player_guess : return "match"
  elif secret_number < player_guess : return "high"
  else: return "low"
  

while should_continue == True:
  if lives == 1: print("This is your last chance!")
  player_guess = int(input("Guess a number between 1 and 100 "))
  result = compare_numbers(secret_number, player_guess)
  if result == "match":
    print("You win! ")
    should_continue = False
  elif result == "high":
    lives -= 1
    print(f"Too high. {lives} lives remaining. ")
  else:
    lives -= 1
    print(f"Too low. {lives} lives remaining. ")
  if lives == 0:
    print(f"You lose! The secret number was {secret_number}")
    should_continue = False
'''

############DEBUGGING#####################

# Describe Problem
""" 
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")    
my_function()
"""
# # Reproduce the Bug
""" 
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
"""
# # Play Computer
""" 
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
print("You are a Gen Z.")
"""
# # Fix the Errors
""" 
age = input("How old are you? ")
if age > 18:
  print("You can drive at age {age}.")
"""

# #Print is Your Friend
""" 
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
"""

# #Use a Debugger
""" 
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
"""
# Debug Even or Odd

""" 
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")  
"""

# Debug Fizz Buzz

""" 
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
"""

""" 
# Higher Lower Game

from HiLo_art import logo
from HiLo_art import vs
from HiLo_game_data import data

should_continue = True

def choose_personality(active_personality):
  choosen = active_personality
  while choosen == active_personality:
    choosen = random.choice(data)
  return choosen

def clear_screen():
  os.system("cls")
  print(logo)
  
old_personality = choose_personality(random.choice(data))
points = 0


clear_screen()
new_personality = choose_personality(old_personality)
print("Compare A: %s, a %s, from %s." % (old_personality["name"], old_personality["description"], old_personality["country"]))
print(vs)
print("Against B: %s, a %s, from %s." % (new_personality["name"], new_personality["description"], new_personality["country"]))
choice = input("Who has more followers? Type \'a\' or \'b\': ")

while should_continue == True:
  if choice == "a":
    if old_personality["follower_count"] > new_personality["follower_count"] : guess = True
    else : guess = False
    
  if choice == "b":
    if new_personality["follower_count"] > old_personality["follower_count"] : guess = True
    else : guess = False
    
  if guess == True:
    points += 1
    clear_screen()
    print(f"You're right! Current score: {points}")
    old_personality = new_personality
    print("Compare A: %s, a %s, from %s." % (old_personality["name"], old_personality["description"], old_personality["country"]))
    print(vs)
    new_personality = choose_personality(old_personality)
    print("Against B: %s, a %s, from %s." % (new_personality["name"], new_personality["description"], new_personality["country"]))
    choice = input("Who has more followers? Type \'a\' or \'b\': ")
      
  else:
    clear_screen()
    print(f"Sorry, that's wrong. Final score: {points}")
    again = input("Do you want to play again? \'y\' \'n\' ")
    if again == "n":
      should_continue = False
      print("Bye!")
    else:
      clear_screen()
      old_personality = choose_personality(random.choice(data))
      new_personality = choose_personality(old_personality)
      print("Compare A: %s, a %s, from %s." % (old_personality["name"], old_personality["description"], old_personality["country"]))
      print(vs)
      print("Against B: %s, a %s, from %s." % (new_personality["name"], new_personality["description"], new_personality["country"]))
      choice = input("Who has more followers? Type \'a\' or \'b\': ")
"""
 
      
      
  

    
    


  
  
  
  