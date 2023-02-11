# Day 10: Functions with outputs

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return (f"{formated_f_name} {formated_l_name}")

formated_string = format_name("tIm", "fhYjsd")
print(formated_string)

# return multiple outputs

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." # terminates functin early
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return (f"{formated_f_name} {formated_l_name}")

#####################

# Exercise 1: Days in month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month == 2 and is_leap(year):
      return 29
  else:
  	return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

##################

# Docstrings

# Return as an early exit

def format_name(f_name, l_name):
	"""Take a first and last name and format it 
	to return the title case version of the name.""" # adds documention to any function
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." # terminates functin early
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return (f"{formated_f_name} {formated_l_name}")


##########################

# Calculator project

# Calculator

from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Put together in a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number? "))
  for symbol in operations:
      print(symbol)
  another_one = True
  
  while another_one:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    ask_continue = input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ")
    if ask_continue == 'n':
      another_one = False
      calculator()
    else:
      num1 = answer

  # You can only call a function within another function if it returns (not prints) its output

calculator()



