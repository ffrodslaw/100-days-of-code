# Day 8: Functions with input

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("Welcome to my code")
  print("I hope you're having a great day.")

greet()

# Function with input

def greet_name(name):
  print(f"Hello {name}!")
  print(f"How are you today, {name}?")

greet_name("Anna")

###################

# Multiple inputs

def greet_with(name, location):
  print(f"Hello {name}!")
  print(f"How is the weather today in {location}?")

greet_with("Bob", "London")
greet_with("London", "Bob") # positional arguments
greet_with(location = "London", name = "Bob") # keyword arguments

###################

# Exercise 1: paint can calculator

#Write your code below this line 👇

import math

def paint_calc(height, width, cover):

    cans = height * width / cover

    # round up
    cans = math.ceil(cans)

    print(f"You'll need {cans} cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

####################

# Exercise 2: prime number checker

#Write your code below this line 👇

def prime_checker(number):

    for i in range(2, number):
        
        is_prime = True
        if number % i == 0:
            # Not a prime number
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#######################

# Caesar cipher part 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):

  encrypted_text = ""
  for i in text:
    pos = alphabet.index(i)
    new_pos = pos + shift
    if new_pos > len(alphabet):
      new_pos -= len(alphabet)
    new_letter = alphabet[new_pos]
    encrypted_text += new_letter
  print(f"The encoded text is {encrypted_text}")

encrypt(text, shift)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

######

# Part 2

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(cypher_text, shift_amount):
  plain_text = ""
  for letter in cypher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
  encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
  decrypt(cypher_text= text, shift_amount = shift)

####################

# Reorganize code:

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
  output_text = ""
  if direction == "decode":
    shift *= -1
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    output_text += alphabet[new_position]
  print(f"The {direction}d text is {output_text}.")
  
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)

######################

# Improve user experience

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}.")


#TODO-1: Import and print the logo from art.py when the program starts.

import art

print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

go_again = True
while go_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_input = input(
        "Do you want to continue? Type 'yes' to go again, 'no' otherwise. ")

    if continue_input == "no":
        go_again = False
        print("Goodbye")
