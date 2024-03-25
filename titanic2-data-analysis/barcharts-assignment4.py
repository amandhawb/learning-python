# 4) How many survived per sex.

import csv
import matplotlib.pyplot as plt

male_survivor = 0
female_survivor = 0

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)

    for line in csv_file:
        if line[1] == '1' and line[3] == 'female':
            female_survivor += 1
        elif line[1] == '1' and line[3] == 'male':
             male_survivor += 1

plt.bar(['Female Survivor', 'Male Survivor'], [female_survivor, male_survivor])
plt.xlabel('COMPARISON OF SURVIVORS PER SEX')
plt.ylabel('COUNT')
plt.title('Comparing survivors by sex in titanic')
plt.show()
