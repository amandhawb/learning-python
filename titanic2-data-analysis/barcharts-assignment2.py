# 2) How many survived per class.

import csv
import matplotlib.pyplot as plt

survived = [0, 0, 0]

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)

    for line in csv_file:
        if line[1] == '1' and line[0] == '1':
            survived[0] += 1
        elif line[1] == '1' and line[0] == '2':
             survived[1] += 1
        elif line[1] == '1' and line[0] == '3':
            survived[2] += 1

print(survived)

plt.bar(['First Class', 'Second Class', 'Third Class'], [survived[0], survived[1], survived[2]])
plt.xlabel('COMPARISON OF SURVIVORS PER CLASS')
plt.ylabel('COUNT')
plt.title('Comparing survivors in each class in titanic')
plt.show()
