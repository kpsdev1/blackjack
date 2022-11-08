# Importing from libraries and declaring global variables
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
    To print text like a typewriter
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
            print(Fore.LIGHTRED_EX + 'Name cannot be blank.\n')

    print("\n\n")
    typewriter("The rules of this BlackJack table are as follows. "
               "Please read Carefully: \n")

    typewriter("1. Closest to 21 wins the hand.\n")
    typewriter("2. If you score above 21, that is bust and the Dealer wins.\n")
    typewriter("4. If you stay, and the Dealer Busts then you win.\n")
    typewriter("4. Getting 21 is counted as BlackJack no matter "
               "how many cards it takes.\n")

    typewriter("5. If the player gets 21 they automatically win.\n")
    typewriter("6. Jack(J), Queen(Q) and King(K) all equal 10,"
               " Ace(A) is either 11 or 1 \ndepending on your score.\n")

    typewriter("7. You will only see one Card for the dealer at the start.\n")
    typewriter("8. The Dealer will Stand(stay) on a hand that is greater than"
               " or equal to 17.\n\n")


def play():
    """
    This funtion asks the user if they are
    ready for the game to start
    by dealing the cards
    """
    time.sleep(1)
    while True:
        start = input('Are you ready for the cards to be dealt?'
                      ' Enter Y for yes.\nOr N to leave : ')
        print()
        if start.upper() == 'Y':
            time.sleep(1)
            break
        elif start.upper() == 'N':
            rprint(f'[yellow]{goodbye}[/yellow]')
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.LIGHTRED_EX + 'Invalid response \n')


def deal_first_two_cards(turn):
    """
    This deals the user their first 2 cards
    """
    for i in range(2):
        cards = random.choice(deck)
        turn.append(cards)
    return turn


def deal_card(turn):
    """
    This deals the a single card
    which is drawn first for the dealer and
    each time the dealer or user Hits.
    """
    card = random.choice(deck)
    turn.append(card)
    return turn


def player_total(turn):
    """
    This is the Function to calculate the players
    total it sets the Jack, Queen and King value
    equal to 10. It sets number cards equal to their value.
    It then sets the Ace equal to 1 and if the total is
    less than or equal to 11 it adds 10 which is what gives
    the Ace the value of 11. This is how it makes the correct
    decision that Ace is either 11 or 1.
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
    This is the Function to calculate the Dealers
    total it sets the Jack, Queen and King value
    equal to 10. It sets number cards equal to their value.
    It then sets the Ace equal to 1 and if the total is
    less than or equal to 11 it adds 10 which is what gives
    the Ace the value of 11. This is how it makes the correct
    decision that Ace is either 11 or 1.
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
    asks the player if they want to Hit or stay
    """
    while score < 21:
        print(Fore.GREEN + '-' * 50 + '\n')
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
            print(Fore.LIGHTRED_EX + 'Invalid response \n')

        print(f"Your cards are {turn} for a total of {score}")
    return Fore.YELLOW + '-' * 50


def dealer_hit_or_stay(score, turn):
    """
    While the dealers score is
    less than 17 it will deal them a card
    as the dealer always stands on 17
    """
    while score < 17:
        deal_card(turn)
        score = dealer_total(turn)
    if score >= 17 and score < 21:
        print(f"Dealers stays with cards {turn} for a total of {score} \n")

    print(f"Dealers Hand was {turn} with a total of {score} \n")


def calculate_winner():
    """
    This function calculates the winner
    and also calls the play another hand function
    """
    print("\n")
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
                      f" and you have {player_score} \n\n")
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
        play_again = input('Do you want to play again, Enter Y for Yes or '
                           'N for No? ')
        if play_again.upper() == 'Y':
            print("\n\n")
            dealer_hand = []
            player_hand = []
            play_hand()
        elif play_again.upper() == 'N':
            rprint(f'[yellow]{goodbye}[/yellow]')
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.LIGHTRED_EX + '\nInvalid response \n')


def play_hand():
    """
    This is the function that plays the hands by calling the
    deal cards functions for the dealer and player and also totals
    their scores and checks the winner
    """
    deal_for_player = deal_first_two_cards
    total_player = player_total
    player_choice = player_hit_or_stay
    deal_for_dealer = deal_card(dealer_hand)
    total_for_dealer = dealer_total

    dealing_message = pyfiglet.figlet_format(
        'Dealing Cards.....', font="slant")
    rprint(f'[green]{dealing_message }[/green]')
    time.sleep(1)

    print("\n")
    print(f"Dealers card is {deal_for_dealer} for "
          f"total of {total_for_dealer(dealer_hand)} \n")
    time.sleep(2)
    print(f"Your cards are {deal_for_player(player_hand)} and "
          f"your total is {total_player(player_hand)} \n")

    print(player_choice(player_score, player_hand))
    calculate_winner()


def main():
    """
    Main function which calls all the
    functions in correct order for the game to run
    """
    greeting()
    play()
    play_hand()


main()
