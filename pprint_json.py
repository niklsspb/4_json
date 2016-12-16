import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        data_dict = json.load(json_file)
    return data_dict


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


file_path = input("Введите имя файла ")
load_data = load_data(file_path)
pretty_print_json(load_data)
if __name__ == '__main__':
    pass
