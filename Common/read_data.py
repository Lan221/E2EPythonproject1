import json
from Config import BASE_DIR

print(BASE_DIR)
print(BASE_DIR + r'/Data/login.json')

def build_data():
        with open(BASE_DIR + r'/Data/login.json',encoding = 'utf-8') as f:
            my_data = json.load(f)
            my_list = []
            for d in my_data:
                d.pop('description')
                my_list.append(tuple(d.values()))
            print(my_list)
        return my_list











