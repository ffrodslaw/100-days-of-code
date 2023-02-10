# Day 9: Dictionaries and nesting

# curly braces denote dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

# retrieve elements
print(programming_dictionary["Bug"])

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."

# empty dictionary
empty_dictionary = {}

# wipe existing dictionary
programming_dictionary = {}

# edit item
programming_dictionary["Bug"] = "A moth in your computer."

# loop through dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

####################
# Exercise 1: Grading program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)

######################

# Nesting

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# nesting a list in a dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"]
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# nesting a dictionary in a dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# dictionary in a list
travel_log = [
  {
    "country": "France", 
   "cities_visited": ["Paris", "Lille", "Dijon"],
   "total_visits" = 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
   "total_visits" = 5
   },
]

#####################

# Exercise 2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities_visited):
    new_dictionary = {
        "country": country,
        "visits": visits,
        "cities": cities_visited
    }
    travel_log.append(new_dictionary)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

###################

# Silent Auction program

from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

print("Welcome to the silent auction program.")

another_one = True

bids = {}

while another_one: 
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bids[name] = bid
  another = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()
  
  if another == "no":
    another_one = False

winning_bet = 0

for bidder in bids:
  if bids[bidder] > winning_bet:
    winning_bet = bids[bidder]
    winner = bidder

print(f"{winner} is the winner with a bid of ${winning_bet}.")