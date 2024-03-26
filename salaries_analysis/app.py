import csv

with open('salaries.csv', 'r') as salaries_file:
    csv_file = csv.reader(salaries_file)
    values = []

    for line in csv_file:
        current_value = int(line[4])
        values.append(current_value)

    average = sum(values) / len(values)
    print("Average of salaries in general: ", round(average, 2))

    salaries_file.seek(0)
    positions = set()

    for line in csv_file:
        positions.add(line[3])

    for title in positions:
        counter_titles = 0
        total_salary = 0
        salaries_file.seek(0)

        for each in csv_file:
            if title == each[3]:
                counter_titles += 1
                total_salary += int(each[4])
        average = round(total_salary / counter_titles, 2)
        print(f'The average salary for {title} is {average}')