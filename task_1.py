import json


FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME, 'r', encoding='utf-8') as input_f:
        json_data = json.load(input_f)
        return round(sum([item.get('score') * item.get('weight') for item in json_data]), 3)


print(task())
