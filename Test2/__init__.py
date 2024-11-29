import json

file_path = r'C:\python\New_SuperHero.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    sorted_superheroes = sorted(data['members'], key=lambda k: k['age'], reverse=True)
    sorted_data = {
        'members': sorted_superheroes,
    }

with open('new_SuperHero.json', 'w') as new_json_file:
    json.dump(sorted_data, new_json_file, indent=4)

def test_test():
    with open('new_SuperHero.json', 'r') as json_file:
        data = json.load(json_file)
        older_than_30 = []
        for superhero in data['members']:
            if superhero['age'] > 30:
                older_than_30.append(superhero['name'])
            assert superhero['age'] >= 30

        if older_than_30:
            print("Супергерои старше 30 лет:")
            for name in older_than_30:
                print(name)
        else:
            print("Нет супергероев старше 30 лет.")

test_test()
