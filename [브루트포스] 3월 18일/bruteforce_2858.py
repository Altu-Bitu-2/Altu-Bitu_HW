# 백준 2858
# 기숙사 바닥

import sys
import math

red, brown = map(int, sys.stdin.readline().split()) # 타일 수 입력
total = red + brown # 타일 총 개수

# ax^2+bx+c=0 의 근의 공식 리턴
def solve_equation(a, b, c):
    return [(-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a]

# equation : width * ((red+4)/2-width) - total = 0
result = solve_equation(1, -(red+4)/2, total)
result.sort(reverse=True) # 내림차순 정렬
print(int(result[0]), int(result[1])) # 소수점 제거 후 출력


"""
width, height라고 할 때
정보 1)
width+height+width+height-4 = red
height = (red+4)/2 - width
정보 2)
width * height = total
-> 2차방정식 풀기
"""