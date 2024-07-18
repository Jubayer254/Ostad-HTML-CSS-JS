import json

filename = 'fruits.json'
with open(filename, 'rt') as fp:
    data = json.loads(fp.read())
    print(data)
    print(type(data))

    if isinstance(data, list):
        for item in data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()  # Adding a newline for better readability
    else:
        print("Unexpected JSON structure")