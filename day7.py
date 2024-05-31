# 튜플 / 집합
# 튜플은 list와 유사하게 생겼으나 불변형.
a_tuple = ('사과', '배', '감')
print(a_tuple)

# 집합 = set
a = [1, 2, 3, 4, 3, 2, 5, 1, 4]

a_set = set(a) # 중복을 제거
print(a_set)

a = ['사과', '감', '배', '수박', '딸기']
b = ['배', '사과', '포도', '참외', '수박']

a_set = set(a)
b_set = set(b)

# 교집합
print(a_set & b_set)

# 합집합
print(a_set | b_set)


student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

# 차집합
a_set = set(student_a)
b_set = set(student_b)
print(a_set - b_set)