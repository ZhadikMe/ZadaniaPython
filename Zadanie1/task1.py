import json

filename = 'input.json'


def task() -> float:
    with open(filename) as file:
        data = json.load(file)
        res = 0
        for num in data:
            res += num['score'] * num['weight']
        return round(res, 3)


print(task())
