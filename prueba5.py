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

# Cofee machine
""" 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

should_continue = True

def check_resources(selection):
  ''' This function checks if there are enough ingredients, prints what is missing
  and returns True or False'''  
  for ing in resources:
    if resources[ing] < int(MENU[selection]["ingredients"].get(ing, 0)):
      print("Sorry, not enough %s" % ing)
      return False
    else:
      return True
    
def remove_resources(selection):
  ''' This function removes used ingredients. '''
  for ing in resources:
    resources[ing] -= int(MENU[selection]["ingredients"].get(ing, 0))
   
def ask_money(selection):
  '''This function asks for coins and returns the total change'''
  print("Please insert %s$ " % MENU[selection]["cost"])
  cents = float(input("How many quarters? ")) * 0.25
  cents += float(input("How many dimes? ")) * 0.1
  cents += float(input("How many nickles? ")) * 0.05
  cents += float(input("How many pennies? ")) * 0.01
  return cents - float(MENU[selection]["cost"])
  


while should_continue == True:
  selection = input(" What would you like? (espresso/latte/cappuccino): ")
  if selection == "report":
    print("Water: %sml" % resources["water"])
    print("Milk: %sml" % resources["milk"])
    print("Coffee: %sg" % resources["coffee"])
    print("Money: %.2f$" % profit)
  elif selection == "off":
    should_continue = False
  else:
    if check_resources(selection) == True:
      change = ask_money(selection)
      if change < 0:
        print("Sorry, not enough money. %.2f$ refunded" % (float(MENU[selection]["cost"]) + change))
      else:
        remove_resources(selection)
        profit += float(MENU[selection]["cost"])
        print("Here\'s your %s ☕ and your change is %.2f$ Enjoy!" % (selection, change))
    
"""    
    