people = [
    {"name":"Harry", "house": "Gryffindor"},
    {"name":"Chao", "house": "Revanclaw"},
    {"name":"Draco", "house": "Slytherin"},
]

for person in people:
    print(person["name"] +" - "+person["house"])

people.sort(key=lambda person:person["name"])

print(people)