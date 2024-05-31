fruits = ['사과', '배', '감', '수박', '딸기']

for fruit in fruits:
    print(fruit)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

print(people[0])
print()

for person in people:
    name = person['name']
    age = person['age']

    if age >= 20:
        print(name, age)
print()

for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)

    if i > 3:
        break


