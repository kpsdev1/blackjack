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
    name = input('Please enter your name? ')
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

def play():
    time.sleep(1)
    while True:
        start = input('Are you ready for the cards to be dealt? Y for yes.\nOr press N to leave : ')
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
            break
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


# check who is the winner
def calculate_winner():
    if player_score == 21 and dealer_score != 21:
        print('You have blackJack')
        print(dealer_score)
    elif player_score > 21:
        print('You have bust')
        print('Dealer wins')
    elif dealer_score == 21 and player_score != 21:
        print('Dealer has blackJack')
        print('Dealer wins')
    elif dealer_score > 21:
        print('Dealer has bust')
        print('You win')
    elif player_score == 21 and dealer_score == 21:
        print('It is a tie both have blackjack')
    elif (21 - dealer_score) > (21 - player_score):
        print('You win')
    elif (21 - dealer_score) < (21 - player_score):
        print('The dealer wins')
    elif dealer_score == player_score:
        print('Its a tie')
    print(f"the dealer has {dealer_score} and you had {player_score}")
    play_another_hand()


# function to play another hand
def play_another_hand():
    print()
    global dealer_hand
    global player_hand
    while True:
        play_again = input('Do you want to play again, Enter Y for Yes or N for No? ')
        if play_again.upper() == 'Y':
            print()
            print()
            print()
            dealer_hand = []
            player_hand = []
            play_hand()
        elif play_again.upper() == 'N':
            print('Goodbye.................')
            time.sleep(1)
            sys.exit()
        else:
            print('Invalid response')
            print()


def play_hand():
    deal_for_player = deal_first_two_cards
    total_player = player_total
    player_choice = player_hit_or_stay

    deal_for_dealer = deal_first_two_cards
    total_for_dealer = dealer_total
    dealer_choice = dealer_hit_or_stay
    first_2_dealer = deal_for_dealer(dealer_hand)

    print(f"Dealer cards are {first_2_dealer} for total of {total_for_dealer(dealer_hand)}")
    print()
    time.sleep(2)
    print(f"Your cards are {deal_for_player(player_hand)} and your total is {total_player(player_hand)}")
    print()
    print(player_choice(player_score, player_hand))
    calculate_winner()


def main():
    # greeting()
    play()
    play_hand()


main()
