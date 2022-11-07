# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import time
import pyfiglet
from rich import print as rprint
import colorama
from colorama import Fore
colorama.init(autoreset=True)
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
goodbye = pyfiglet.figlet_format('GoodBye...........', font="slant")


def typewriter(words):
    """
    To print text like a type writer
    """
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)


def greeting():
    """
    This is the greeting function
    that asks the Users name and greets them
    """
    welcome_sign = pyfiglet.figlet_format(
        'WELCOME TO THE BLACKJACK TABLE', font="slant")
    rprint(f'[blue]{welcome_sign}[/blue]')

    # Checking to make sure that users name is not blank
    while True:
        name = input('Please enter your name? ').strip()
        if name != '':
            typewriter(f"Hi {name}, Welcome to the BlackJack table. Please"
                       " have a read of the \nrules below before playing.")
            break
        else:
            print()
            print(Fore.LIGHTRED_EX + 'Name cannot be blank.')
            print()

    print()
    print()
    typewriter("The rules of this BlackJack table are as follows. "
               "Please read Carefully:")
    print()
    typewriter("1. Closest to 21 wins the hand.")
    print()
    typewriter("2. If you score above 21, that is bust and the Dealer wins.")
    print()
    typewriter("4. If you stay, and the Dealer Busts then you win.")
    print()
    typewriter("4. Getting 21 is counted as blackJack no matter "
               "how many cards it takes.")
    print()
    typewriter("5. If the player gets 21 they automatically win.")
    print()
    typewriter("6. Jack(J), Queen(Q) and King(K) all equal 10,"
               " Ace(A) is either 11 or 1 \ndepending on your score.")
    print()
    typewriter("7. You will only see one Card for the dealer at the start.")
    print()


def play():
    """
    This funtion asks the user if they are
    ready for the game to start
    by dealing the cards
    """
    time.sleep(1)
    while True:
        print()
        start = input('Are you ready for the cards to be dealt? '
                      'Y for yes.\nOr press N to leave : ')
        print()
        if start.upper() == 'Y':
            time.sleep(1)
            break
        elif start.upper() == 'N':
            rprint(f'[yellow]{goodbye}[/yellow]')
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.LIGHTRED_EX + 'Invalid response')
            print()


def deal_first_two_cards(turn):
    """
    This deals the user and dealer the first 2 cards
    """
    for i in range(2):
        cards = random.choice(deck)
        turn.append(cards)
        deck.remove(cards)
    return turn


def deal_card(turn):
    """
    This deals the next cards
    """
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    return turn


def player_total(turn):
    """
    This is the Function
    to calculate the players total
    """
    global player_score
    player_score = 0
    for ind in turn:
        if 'A' == ind:
            player_score += 1
        if 'J' == ind or 'Q' == ind or 'K' == ind:
            player_score += 10
        if 'J' != ind and 'Q' != ind and 'K' != ind and 'A' != ind:
            player_score += ind
    if 'A' in player_hand and player_score <= 11:
        player_score += 10
    return player_score


def dealer_total(turn):
    """
    This is the Function
    to calculate dealers total
    """
    global dealer_score
    dealer_score = 0
    for ind in turn:
        if 'A' == ind:
            dealer_score += 1
        if 'J' == ind or 'Q' == ind or 'K' == ind:
            dealer_score += 10
        if 'J' != ind and 'Q' != ind and 'K' != ind and 'A' != ind:
            dealer_score += ind
    if 'A' in dealer_hand and dealer_score <= 11:
        dealer_score += 10
    return dealer_score


def player_hit_or_stay(score, turn):
    """
    If the score is less than 21 the function
    asks the player if they want to it or stay
    """
    while score < 21:
        print(Fore.GREEN + '-' * 50)
        print()
        choice = input(
            'Do you want to Hit or Stay, Enter H for Hit or S for Stay? ')
        print()
        if choice.upper() == 'H':
            deal_card(turn)
            score = player_total(turn)
            print()
        elif choice.upper() == 'S':
            dealer_hit_or_stay(dealer_score, dealer_hand)
            break
        else:
            print(Fore.LIGHTRED_EX + 'Invalid response')
            print()
        print(f"Your cards are {turn} for a total of {score}")
    return Fore.YELLOW + '-' * 50


def dealer_hit_or_stay(score, turn):
    """
    While the dealers score is
    less than 17 it will deal them a card
    as the deal always stnds on 17
    """
    while score < 17:
        deal_card(turn)
        score = dealer_total(turn)
    if score >= 17 and score < 21:
        print(f"Dealers stays with cards {turn} for a total of {score}")
        print()
    print(f"Dealers Hand was {turn} with a total of {score}")
    print()


def calculate_winner():
    """
    This function calculates the winner
    and also calls the play another hand function
    """
    print()
    print()
    if player_score == 21 and dealer_score != 21:
        print(Fore.GREEN + 'You have blackJack, You Win')
    elif player_score > 21:
        print(Fore.RED + 'You have bust, Dealer Wins')
    elif dealer_score == 21 and player_score != 21:
        print(Fore.RED + 'Dealer has blackJack, Dealer wins')
    elif dealer_score > 21:
        print(Fore.GREEN + 'Dealer has bust, You Win')
    elif player_score == 21 and dealer_score == 21:
        print(Fore.MAGENTA + 'It is a tie both have blackjack')
    elif (21 - dealer_score) > (21 - player_score):
        print(Fore.GREEN + 'You Win')
    elif (21 - dealer_score) < (21 - player_score):
        print(Fore.RED + 'The Dealer Wins')
    elif dealer_score == player_score:
        print(Fore.MAGENTA + 'Its a tie')
    print(Fore.BLUE + f"The dealer has {dealer_score}"
                      f" and you have {player_score}")
    print()
    print()
    print(Fore.YELLOW + '-' * 50)
    play_another_hand()


def play_another_hand():
    """
    This is a function that ask the player if they
    want to play another hand
    """
    print()
    global dealer_hand
    global player_hand
    while True:
        play_again = input('Do you want to play again, Y for Yes, N for No? ')
        if play_again.upper() == 'Y':
            print()
            print()
            print()
            dealer_hand = []
            player_hand = []
            play_hand()
        elif play_again.upper() == 'N':
            rprint(f'[yellow]{goodbye}[/yellow]')
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.LIGHTRED_EX + 'Invalid response')
            print()


def play_hand():
    deal_for_player = deal_first_two_cards
    total_player = player_total
    player_choice = player_hit_or_stay

    deal_for_dealer = deal_card(dealer_hand)
    total_for_dealer = dealer_total
    dealing_message = pyfiglet.figlet_format(
        'Dealing Cards.....', font="slant")
    rprint(f'[green]{dealing_message }[/green]')
    time.sleep(1)
    print()
    print()
    print(f"Dealer cards are {deal_for_dealer} for "
          f"total of {total_for_dealer(dealer_hand)}")
    print()
    time.sleep(2)
    print(f"Your cards are {deal_for_player(player_hand)} and "
          f"your total is {total_player(player_hand)}")
    print()
    print(player_choice(player_score, player_hand))
    calculate_winner()


def main():
    greeting()
    play()
    play_hand()


main()
