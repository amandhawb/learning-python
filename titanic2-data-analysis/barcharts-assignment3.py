# 3) How many did not survive per class.

import csv
import matplotlib.pyplot as plt

not_survived = [0, 0, 0]

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)

    for line in csv_file:
        if line[1] == '0' and line[0] == '1':
            not_survived[0] += 1
        elif line[1] == '0' and line[0] == '2':
             not_survived[1] += 1
        elif line[1] == '0' and line[0] == '3':
            not_survived[2] += 1

plt.bar(['First Class', 'Second Class', 'Third Class'], [not_survived[0], not_survived[1], not_survived[2]])
plt.xlabel('COMPARISON OF NOT SURVIVORS PER CLASS')
plt.ylabel('COUNT')
plt.title('Comparing not survivors in each class in titanic')
plt.show()
