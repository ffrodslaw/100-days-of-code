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






