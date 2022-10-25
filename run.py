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


def greeting():
    typewriter(f"Hi {name}, welcome to the blackJack table.")
    print()
    time.sleep(1)
    while True:
        start = input('Are you ready to Play? Type Y for Yes. Or N to leave : ')
        if start.upper() == 'Y':
            print('Dealing cards.......')
            time.sleep(1)
            break
        elif start.upper() == 'N':
            print('Goodbye.................')
            time.sleep(1)
            sys.exit()
        else:
            print('Invalid response')
            print()

greeting()