# 5) How many did not survive per sex.

import csv
import matplotlib.pyplot as plt

male_not_survivor = 0
female_not_survivor = 0

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)

    for line in csv_file:
        if line[1] == '0' and line[3] == 'female':
            female_not_survivor += 1
        elif line[1] == '0' and line[3] == 'male':
            male_not_survivor += 1

plt.bar(['Female Not Survivor', 'Male Not Survivor'], [female_not_survivor, male_not_survivor])
plt.xlabel('COMPARISON OF NOT SURVIVORS PER SEX')
plt.ylabel('COUNT')
plt.title('Comparing not survivors by sex in titanic')
plt.show()
