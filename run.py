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

# players total
def player_total(turn):
    global player_score
    player_score = 0
    for ind in turn:
        if 'J' == ind or 'Q' == ind or 'K' == ind:
            player_score += 10
        if 'A' == ind:
            player_score += 11
        if 'J' != ind and 'Q' != ind and 'K' != ind and 'A' != ind:
            player_score += ind
    return player_score


# Dealers total
def dealer_total(turn):
    global dealer_score
    dealer_score = 0
    for ind in turn:
        if 'J' == ind or 'Q' == ind or 'K' == ind:
            dealer_score += 10
        if 'A' == ind:
            dealer_score += 11
        if 'J' != ind and 'Q' != ind and 'K' != ind and 'A' != ind:
            dealer_score += ind
    return dealer_score


# hit or stay for the player
def player_hit_or_stay(score, turn):
    while score < 21:
        choice = input(
            'Do you want to Hit or Stay, Enter H for Hit or S for Stay? ')
        if choice.upper() == 'H':
            deal_card(turn)
            score = player_total(turn)
            print(f"{turn} for a total of {score}")
        elif choice.upper() == 'S':
            dealer_hit_or_stay(dealer_score, dealer_hand)
            return f"Your cards are {turn} for a total of {score} "

# Hit or stay for the dealer
def dealer_hit_or_stay(score, turn):
    while score < 17:
        deal_card(turn)
        score = dealer_total(turn)
    if score >= 17 and score < 21:
        print(f"Dealers  stays for with cards {turn} for a total of {score} ")
    print(f"Dealers Hand was {turn} with a total of {score}")
    print()



print(f"Dealer cards are {deal_first_two_cards(dealer_hand)} for total of {dealer_total(dealer_hand)}")
print()
print(f"Player cards are {deal_first_two_cards(player_hand)} for total of {player_total(player_hand)}")
player_hit_or_stay(player_score, player_hand)
print()
