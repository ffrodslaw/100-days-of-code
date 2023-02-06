# Day 5: Loops, range, code blocks
###################

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
  print(fruits)

# indentation importnat

################

# Exercise 1: height average

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

sum = 0
length = 0

for i in student_heights:
    sum += i 
    length += 1

avg = round(sum / length)

print(avg)

############################

# Exercise 2: Highest score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = student_scores[0]

for i in student_scores:
    if i > highest_score:
        highest_score = i
    else:
        highest_score = highest_score

print("The highest score in the class is: " + str(highest_score))

##############################

# range

for number in range(1,11):  # loop from 1 to 10
  print(number)

# add up all number from 1 to 100

total = 0
for number in range(1, 101):
  total += number

print(total)

##############################

# Exercise 3: adding even numbers

#Write your code below this row 👇

even_total = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_total += i
    else:
        even_total = even_total
    
print(even_total)

# alternative, you can change the step size in range --> range(1, 101, 2)

###############################

# Exercise 4: Fizzbuzz

#Write your code below this row 👇

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

##############################

# Project: random password generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for i in range(1, nr_letters + 1):
  add = random.choice(letters)
  password = password + add

for i in range(1, nr_symbols + 1):
  add = random.choice(symbols)
  password = password + add

for i in range(1, nr_numbers + 1):
  add = random.choice(numbers)
  password = password + add

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = "".join(random.sample(password, len(password)))
# randomly change order of characters in previously generated password
# random.shuffle only works with items in list

print(password)





