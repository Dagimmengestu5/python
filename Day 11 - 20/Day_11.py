# BlackJack Game

import random
import os 
logo = ''' ___   ___   ___   ___   ___ 
 |A  | |K  | |Q  | |J  | |10 |
 |(`)| |(`)| |(`)| |(`)| |(`)|
 |_\_| |_\_| |_\_| |_\_| |_\_|
  ___   ___   ___   ___   ___   ___ 
 |A  | |2  | |3  | |4  | |5  | |6  |
 | /\| | /\| | /\| | /\| | /\| | /\|
 |_\/| |_\/| |_\/| |_\/| |_\/| |_\/|
  ___   ___   ___   ___   ___   ___   ___
 |A  | |2  | |3  | |4  | |5  | |6  | |7  |
 | ^ | | ^ | | ^ | | ^ | | ^ | | ^ | | ^ |
 |(,)| |(,)| |(,)| |(,)| |(,)| |(,)| |(,)| 
'''


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate the score of the given cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose. opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "you went over. you lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    end_game = False

    for l in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards},   current score:   [{user_score}]")
        print(f"    Computer's first card: [{computer_cards[1]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
                os.system('cls' if os.name == 'nt' else 'clear')
                play_game()
while input != "y":
    print("/////////ok/////") # i don't now this messsege is loop nonstope
     