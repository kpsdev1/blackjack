# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import time

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
name = input('Please enter your name? ')

def typewriter(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)
       
typewriter(f"Hi {name}, Welcome to the blackJack table.")
