import csv

def calculate_percentage(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        total_lines = 0
        count = 0
        for line in csv_reader:
            total_lines += 1
            last_value = line[-1]
            if last_value.strip() == '1':
                count += 1
        percentage = (count / total_lines) * 100
        return percentage

file_path = 'test.csv'
percentage = calculate_percentage(file_path)

with open('output.txt', 'w') as file:
    file.write(f"Percentage: {percentage}%")