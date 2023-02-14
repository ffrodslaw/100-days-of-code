#####################
 # Day 14
 # Project: higher or lower game

import art
from game_data import data
import random
from replit import clear

def check_answer(guess, count1, count2):
  if count1 > count2:
    return guess == "A"
  else:
    return guess == "B"

def higher_lower():

  print(art.logo)
  score = 0
  game_over = False
  sample = random.sample(data, 2)
    
  while not game_over:

  # switching positions and resampling the second account
  # to make sure account2 is account1 in the next round
    acc1 = sample[1]
    acc2 = random.choice(data)
  
      # making sure the accounts are not the same
    while acc1 == acc2:
      acc2 = random.choice(data)
        
    name1 = acc1['name']
    count1 = int(acc1["follower_count"])
    desc1 = acc1["description"]
    country1 = acc1["country"]
    
    name2 = acc2['name']
    count2 = int(acc2["follower_count"])
    desc2 = acc2["description"]
    country2 = acc2["country"]
      
    print(f"Compare A: {name1}, a {desc1}, from {country1}.")
    print(art.vs)
    print(f"Against B: {name2}, a {desc2}, from {country2}.")
    
    guess = input("Who has more followers? Type 'A' or 'B'. ")
    correct_answer = check_answer(guess, count1, count2)
    
    clear()
    print(art.logo)
    if correct_answer:
      score += 1
      print(f"You're right! Your current score is {score}.")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Your final score is {score}.")

higher_lower()    
                                                                   