# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-u_I7hV0VhjesFRFu5Txzj4seMG2OjdQ
"""

# 1. Create a list named 'students' containing tuples, where each tuple
# represents a student and contains the following information: student name,
# age, grade,  and favorite subject.

students = [
    ('amandha', '23', 'GPA 4', 'programming development'),
    ('wellignton', '33', 'GPA 3', 'network systems')
]

# 2. Print out the list of students.

print(students)

# 3. Ask the user to input a new student's information and add
# it to the 'students' list as a tuple.

user_name = input("Enter a new student's information separed by ','")
user_name_tuple = tuple(map(str, user_name.split(',')))
students.append(user_name_tuple)

# 4. Print out the updated list of students.

print(students)

# 5. Create a new list named 'student_names' containing only the names of
# the students from the 'students' list. (Use a loop)

student_names = []

for student in students:
  student_names.append(student[0])

# 6. Print the 'student_names' list.
print(student_names)

# 7. Print each list item individually
for student in student_names:
  print(student)