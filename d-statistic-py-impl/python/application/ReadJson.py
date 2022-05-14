import json

json_file: str = str(input())

json_open = open(json_file, 'r')

json_load = json.load(json_open)

for v in json_load.values():
    print(v)
