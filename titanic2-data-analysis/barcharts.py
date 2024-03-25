import csv
import matplotlib.pyplot as plt

males = 0
females = 0

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)
    line_count = 0

    for line in csv_file:
        if line_count > 0:
            if line[3] == 'male':
                males += 1
            else:
                females += 1
        line_count += 1

plt.bar(['Males', 'Females'], [males, females])
plt.xlabel('SEX')
plt.ylabel('COUNT')
plt.title('Comparing males and females in titanic')
plt.show()
