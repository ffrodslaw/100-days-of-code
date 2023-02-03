# Topics: conditional statements, logical operators, elif

# Theme park ticket box
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120 :
  print("You can ride the rollercoaster.")
else:
  print("You cannot ride the rollercoaster.")

####################

# Exercise 1: even or odd

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# modulo operator % gives the remainder of division

rem = number % 2

if rem == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

###################

# Add age condition to rollercoaster code
# nested if statement

if height > 120 :
	if age > 18:
		print("You have to pay $12.")
	else: 
		print("You have to pay $7.")
else:
	print("Sorry, you are too short to ride.")

## If statement with multiple categories:

if height > 120 :
	if age > 18:
		print("You have to pay $12.")
	elif age <= 12:
		print("You have to pay $5.")
	else: 
		print("You have to pay $7.")
else:
	print("Sorry, you are too short to ride.")


###################

# Exercise 2: BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2, 0)

if bmi < 18.5:
    int = "are underweight"
elif bmi > 18.5 and bmi < 25:
    int = "have a normal weight"
elif bmi > 25 and bmi < 30:
    int = "are slightly overweight"
elif bmi > 30 and bmi < 35:
    int = "are obese"
else:
    int = "are clinically obese"

print(f"Your BMI is {bmi}, you {int}.")    

#####################

# Exercise 3: Leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap year.")
    elif year % 400 != 0 and year % 100 != 0:
        print("Leap year.")   
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


#######################

# Back to ticket prices

if height > 120 :
	age = int(input("What is your age?"))
	if age > 18:
		price = 12
	elif age <= 12:
		price = 5
	else: 
		price = 7 
	photo = input("Do you want a photo taken? Y or N.")
	if photo == "Y":
		price += 3
	else:
		price += 0
	print(f"You have to pay ${price}.")
else:
	print("Sorry, you are too short to ride.")

#################

# Exercise 4: Pizza prices

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
else:
    price = price
if extra_cheese == "Y":
    price += 1
else:
    price = price

print(f"Your final bill is ${price}.")

###########################

# Exercise 5: Love score

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2
names_lower = names.lower()

t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")

true = str(t + r + u + e)
love = str(l + o + v + e)

score = int(true+love)

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

##########################

# Final project: treasure hunt

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

ans1 = input("Do you want to go left or right? ").lower()
if ans1 == "right":
  print("You fell into a hole. Game over :(")
else:
  ans2 = input("You made it to a lake. Do you want to swim or wait for a boat? ").lower()
  if ans2 == "wait":
    ans3 = input("You are on an island and see a house with three doors. Which door do you open? Red, yellow, or blue? ").lower()
    if ans3 == "red" :
      print("The room is on fire. Game over :(")
    elif ans3 == "yellow":
      print("The room is full of treasure. You win!")
    elif ans3 == "blue":
      print("The room is full of squirrels that eat you. Game over :(")
    else:
      print("Game over!")
  else:
    print("You were eaten by trout. Game over :(")
