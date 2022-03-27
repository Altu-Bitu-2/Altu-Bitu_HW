# 백준 11723
# 집합

import sys

input = sys.stdin.readline

m = int(input()) # 수행해야 하는 연산의 수 m 입력

s = set()

for i in range(m):
    calculate = input().rstrip().split()
    if len(calculate) == 1: # 명령어가 한 개일 경우 -> all, empty
        if calculate[0] == 'all':
            s = set(range(1, 21))

        elif calculate[0] == 'empty':
            s = set()

    else: # 명령어 입력이 2개 일 경우 -> ex) add x, remove x, check x, toggle x
        number = int(calculate[1]) # 두 번째 입력을 int로 바꿔주기
        if calculate[0] == 'add': 
            if number in s:
                continue
            else:
                s.add(number)

        elif calculate[0] == 'remove':
            if number not in s:
                continue
            else:
                s.remove(number)

        elif calculate[0] == 'check':
            print(1 if number in s else 0)

        elif calculate[0] == 'toggle':
            if number in s:
                s.remove(number)
            else:
                s.add(number)

