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
        time.sleep(0.1)


def greeting():
    typewriter(f"Hi {name}, welcome to the blackJack table.")
    print()
    typewriter("The rules of this BlackJack table are as follows. Please read Carefully : ")
    print()
    typewriter("1. Closest to 21 wins the hand")
    print()
    typewriter("2. If either the computer or player goes above 21, they are consider bust and they lose the hand.")
    print()
    typewriter("3. If either the player or the computer gets to 21 no matter how many \ncards it takes this is counted as blackjack ")
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


# This deals the user and dealer the first 2 cards
def deal_first_two_cards(turn):
    for i in range(2):
        cards = random.choice(deck)
        turn.append(cards)
    return turn

# This deals the next cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    return turn

print(f"Players cards are {deal_first_two_cards(player_hand)}")
print(f"Dealers cards are {deal_first_two_cards(dealer_hand)}")
print(f"Players next card {deal_card(player_hand)}")

