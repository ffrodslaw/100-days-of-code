# Day 4: random module, lists
###############################

import random

random_integer = random.randint(1, 10)

print(random_integer)

# you can import another script (.py) with import as well

# random floating point number

random_float = random.random()
print(random_float)

random_float2 = random.random() * 5    # random float between 0 and 5
print(random_float2)

############
# Exercise 1: flip a coin

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

coin = random.randint(0,1)

if coin == 0:
    result = "Heads"
else:
    result = "Tails"

print(result)
  

###############################

# Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

# order matters
 
print(states_of_america[2])
print(states_of_america[-3]) # counts from the back

number = 2
print(states_of_america[number])

# change an item
states_of_america[1] = "Pencilvania"
print(states_of_america)

# add another item
states_of_america.append("Annaland")
print(states_of_america)

# add multiple individual items
states_of_america.extend(["Annaland", "Angelaland"])
print(states_of_america)


########################

# Excercise 2: Bankers' roulette

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

random = random.randint(0, len(names) - 1)

print(names[random] +" is going to buy the meal today!")

#########################


#nested list

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


########################

# Exercise 3: treasure map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

number_column = int(str(position)[0]) - 1
number_row = int(str(position)[1]) -1

map[number_row][number_column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

##################

# Project: rock paper scissors game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

hands = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))

if player_choice < 0 or player_choice > 2:
  print("You typed an invalid number, you lose!")
else:
  computer_choice = random.randint(0, 2)
  
  if player_choice == computer_choice:
    print(hands[player_choice] + "\n" + hands[computer_choice] + "\n" + "It's a draw!")
  elif player_choice == computer_choice - 1:
    print(hands[player_choice] + "\n" + hands[computer_choice] + "\n" + "You lose!")
  else:
    print(hands[player_choice] + "\n" + hands[computer_choice] + "\n" + "You win!")
   