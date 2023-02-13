# Day 12: Namespaces and scope

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope

def drink_potion():
  potion_strength = 2  # is only valid within the function
  print(potion_strength)

drink_potion()
# print(potion_strength) # error not defined

# Global scope
player_health = 10  # valid anywhere

def game():
  def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion() # error since it only exists in game()

# There is no block scope

if 3 > 2:
  a_variable = 10   # will still be a global variable


game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # error because it is nested in create_enemy()

# local scope only applies when variable is in a new function

enemies = 1
def increase_enemics():
  global enemies  # explicitly calls a global variable
  enemies += 1

# modifying globale variable within a function is not recommended

#############

# Constants

PI = 3.141592
URL = "https://www.google.com"

# naming convention: constants to be named in all caps

####################

# Final project: number guesser

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  tries_left = 10
else:
  tries_left = 5
number = random.choice(range(100))

while tries_left > 0:
  print(f"You have {tries_left} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
  elif guess < number:
    print("Too low.\nGuess again.")
    tries_left -= 1
  else:
    print("Too high.\nGuess again.")
    tries_left -= 1
  if tries_left == 0:
    print(f"You've run out of guess, you lose. The correct number was {number}.")

