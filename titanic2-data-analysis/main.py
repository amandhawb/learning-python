import csv

with open('titanic2.csv', 'r') as my_file:
    csv_file = csv.reader(my_file)
    line_count = 0

    passenger_female_classes = [0,0,0]
    passenger_male_classes = [0,0,0]

    for line in csv_file:
        if line_count > 0:
            if line[3] == 'female' and line[0] == '1':
                passenger_female_classes[0] += 1
            elif line[3] == 'female' and line[0] == '2':
                passenger_female_classes[1] += 1
            elif line[3] == 'female' and line[0] == '3':
                passenger_female_classes[2] += 1

            if line[3] == 'male' and line[0] == '1':
                passenger_male_classes[0] += 1
            elif line[3] == 'male' and line[0] == '2':
                passenger_male_classes[1] += 1
            elif line[3] == 'male' and line[0] == '3':
                passenger_male_classes[2] += 1
        line_count += 1

print('Total female passengers on first class', passenger_female_classes[0])
print('Total female passengers on second class', passenger_female_classes[1])
print('Total female passengers on third class', passenger_female_classes[2])

print('Total male passengers on first class', passenger_male_classes[0])
print('Total male passengers on second class', passenger_male_classes[1])
print('Total male passengers on third class', passenger_male_classes[2])