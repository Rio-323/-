def cal(a, b):
    return a + 2 * b

result = cal(1, 2)
print(result)


def cal1(a, b = 2):
    return a + 2 * b

result = cal1(1, 3)
print(result)

def cal2(*args):
    for name in args:
        print(f'{name} 밥먹어라~')

result = cal2('영수', '철수', '영희')

# 딕셔너리로 만들어줌
def cal3(**kwargs):
    print(kwargs)

cal3(name = 'bob', age = 30, height = 100)
