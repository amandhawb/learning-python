# 1) How many survived versus not survived:

import csv
import matplotlib.pyplot as plt

survived = 0
not_survived = 0

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)

    for line in csv_file:
        if line[1] == '1':
            survived += 1
        elif line[1] == '0':
            not_survived += 1

plt.bar(['Survived', 'Not survived'], [survived, not_survived])
plt.xlabel('COMPARISON OF SURVIVORS')
plt.ylabel('COUNT')
plt.title('Comparing survivors and not survivors in titanic')
plt.show()
