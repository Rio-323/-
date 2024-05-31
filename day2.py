first_name = "sean"
last_name = "kim"

print(first_name + last_name)


a = 2
b = a
print(b) # b = 문자열 a 임

print(str(a))

text = 'abcdefghijk'

result = len(text)
result1 = text[:3]
result2 = text[3:]
result3 = text[3:8]

print(text)
print(result)
print(result1)
print(result2)
print(result3)

myemail = 'abc@sparta.co'
result = myemail.split('@')[1].split('.')[0]

print(result)
