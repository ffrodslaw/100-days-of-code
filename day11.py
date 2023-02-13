# Day 11: Capstone project - Blackjack program

import random
from art import logo
from replit import clear

def calculate_score(card):
  card_score = sum(card)
  if (11 in card) and card_score > 21:
    card_score -= 10
  if card_score == 21:
      card_score = 0
  return card_score

def determine_winner(player_score, computer_score):
  if computer_score == 0:
    print("You lost, the computer hit Blackjack.")
  elif player_score == 0:
    print("You win, you hit Blackjack!")
  elif player_score > 21:
    print("You lose, your score is larger than 21.")
  elif computer_score > 21:
    print("You win, the computer's score is larger than 21.")
  elif player_score == computer_score:
    print("It's a draw.")
  elif player_score > computer_score:
    print("You win! :)")
  else:
    print("You lose! :(")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

  print(logo)
  
  keep_playing = True
  player_hand = []
  computer_hand = []
  for _ in range(2):
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
  
  while keep_playing:
    
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")   
    
    if computer_score == 0 or player_score == 0 or player_score > 21:
      keep_playing = False
    else:
      play_again = input("Do you want to draw another card, 'y' or 'n'? ")
      if play_again == "n":
        keep_playing = False
      elif play_again == "y":
        print(player_hand)
        player_hand.append(random.choice(cards))
        print(player_hand)

   # computer plays and keeps drawing cards until the score is > 16
  while computer_score < 17 and computer_score != 0:
    computer_hand.append(random.choice(cards))
    computer_score = calculate_score(computer_hand)

  # final results
  print(f"Your final hand is {player_hand}, your score is {player_score}.")
  print(f"The computer's final hand is {computer_hand}, its score is {computer_score}.")
  determine_winner(player_score, computer_score)

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_game == "y":
  clear()
  blackjack()


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


