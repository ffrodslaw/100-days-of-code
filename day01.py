# 100 days of code
# Day 1

# topics: print, input, variables

############

# printing

print("Hello" + " " + "Anna\n") # concatenation

# spaces/indentations are important 

print("Hello " + input("What is your name? ") + "!")


# variables

# ask for name and calculate number of characters
name = input("What is your name? ")

print(len(name))

name = "Angela"
print(name)

length = len(name)

print(length)

# project of the day: band name generator

# Instructions:
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Hello and welcome to my band name generator!\n")
city = input("What city did you grow up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name is " + city + " " + pet + "s!")