# Day 13: Debugging

############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 20): # range does not include upper limit
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # index starts at 0 and should end at 5
print(dice_imgs[dice_num]) # sometimes gives error

# # Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994: # no output for 1994
  print("You are a Gen Z.")

# # Fix the Errors
age = input("How old are you?") # needs to be an integer: int()
if age > 18:
  print(f"You can drive at age {age}.")    # needs to be indented

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # needs to be a single =
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)  # needs to be indented to run for every element in list
  print(b_list)

mutate([1,2,3,5,8,13])

###############

# Exercise 1

number = int(input("Which number do you want to check?"))

if number % 2 == 0: # needed to be double = for conditions
  print("This is an even number.")
else:
  print("This is an odd number.")
  
###############

# Exercise 2

year = int(input("Which year do you want to check?")) # needed to be an integer

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
 ##################

 # Exercise
 
  for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # and not or
    print("FizzBuzz")
  elif number % 3 == 0: # elif not if
    print("Fizz")
  elif number % 5 == 0: # elif not if
    print("Buzz")
  else:
    print([number])
