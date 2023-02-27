# Day 25: List comprehension

import random
import pandas

numbers = [1,2,3]
add_one = [n +1 for n in numbers]
print(add_one)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

range_list = range(1, 5)
doubled = [n * 2 for n in range_list]
print(doubled)

# conditions
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) < 5]
long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)

#################

# Dictionary comprehension

# dictionary of students as keys with random scores as values
student_score = {student:(random.randint(1,100)) for student in names}

passed_students = {student:score for (student, score) in student_score.items() if score > 60}

print(passed_students)

#################

# Looping through a data frame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

# for (key, value) in student_df.items():
#     print(key)

# Loop through rows of a df
for (index, row) in student_df.iterrows():
    print(row.student)