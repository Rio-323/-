def hello():
    print('안녕')

hello()
#-----------------------------------

def sum(a, b):
    return a + b

result = sum(1, 2)
print(result)
#-----------------------------------

def bus_rate(age):
    if age > 65:
        print('무료입니다.')
    elif age > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')

bus_rate(35)
#-----------------------------------

def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여성')
    else:
        print('남성')
#-----------------------------------