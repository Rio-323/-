# Python 기초 공부 - 입출력
# input() -> 입력값 한 줄을 읽어옴.
a = input('값을 입력해주세요 : ')
print(a)

import sys
a = sys.stdin.readline() # 속도가 빨라서 input() 대신 쓰기도 함.
print(a)