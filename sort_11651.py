# 백준 11651
# 좌표 정렬하기 2

import sys

input = sys.stdin.readline

number = int(input()) # 점의 개수 입력
dot = []

for i in range(number): # 점의 개수만큼 반복
    x, y = map(int, input().split())
    dot.append((x, y))

# print(dot)
dot.sort(key=lambda x:(x[1], x[0]))


for i in range(0, len(dot)):
    print("{0} {1}".format(dot[i][0], dot[i][1]))
# print(dot[1][0]) 리스트 몇 번째에 튜플 몇 번째 요소인지
# 튜플 함수는 리스트와 비슷한데 몇 개는 쓰지 못함

# list = [(1, 2), (4, 2), (0, 7), (6, 9)]
# list.sort(key=lambda x:x[0])
# print(list)