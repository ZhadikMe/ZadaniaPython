import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter=',', lineterminator='\n')
        data = list(reader)

    json_data = json.dumps(data, indent=4)

    with open(OUTPUT_FILENAME, 'w') as output_file:
        output_file.write(json_data)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
