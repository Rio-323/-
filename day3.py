# 리스트 = 순서가 중요
# 딕셔너리 = 키 : 값

a_list = ['사과', '배', '감']
print(a_list[0])

b_list = [3, 4, 5, 6, 7, 2, 1]
b_list.append(99)
print(b_list)

b_list.sort()
print(b_list)

result = 99 in a_list
print(result)

a_dict = {'name' : 'bob', 'age' : 27, 'friend' : ['영희', '철수']}
print(a_dict['name'])
print(a_dict['age'])
print(a_dict['friend'])
print(a_dict['friend'][1])

a_dict['height'] = 100
print(a_dict)

result = 'height' in a_dict
print(result)

people = [{'name' : 'bob', 'age' : 27},
          {'name' : 'john', 'age' : 30}]
print(people[1]['age'])


# smith의 science 점수 출력
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people[2]['score']['science'])