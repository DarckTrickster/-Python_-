import json

INPUT_FILENAME = "input.json"

def task() -> float:

    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)


    total_sum = sum(item["score"] * item["weight"] for item in data)


    return round(total_sum, 3)


print(task())
