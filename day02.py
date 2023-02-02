#Data Types

# String

print("Hello"[4]) # subscripting

print("123"[2])

print("123" + "345") # concatenation

# Integer

print(123 + 345)

123_456_789 # python will ignore underscores

# Floating

3.141592

# Boolean

True
False


# Check what kind of vaeriable we have

num_char = len(input("What is your name?"))

print(type(num_char))

# Convert

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")


####

a = 123
print(type(a))

print(70 + float("100.5"))


###############
# Exercise 1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_num = two_digit_number[0]
second_num = two_digit_number[1]

result = int(first_num) + int(second_num)

print(result)

###################################

# Mathematical operators

3 + 5
7 - 2
3 * 2
6 / 3
2 ** 2 # exponent

# order

print(3 * (3 + 3) / 3 - 3)

###################################
# Exercise 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_fl = float(height)
weight_fl = float(weight)

bmi = weight_fl / height_fl ** 2
bmi_int  = int(bmi)

print(bmi_int)

###################################

# number manipulation

print(round(8 / 3, 2))

print(8 // 3) # floor division, result is integer

score = 1
score += 1 # add 1 to score

# combine different data types

score = 0
height = 1.8
isWinning = True

#f-string

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")

##################################
# Exercise 3

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

####################################

# Final project

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

share = round(float(total) / int(people) * (1 + int(tip)/100), 2)

print(f"Each person should pay: ${share}")

