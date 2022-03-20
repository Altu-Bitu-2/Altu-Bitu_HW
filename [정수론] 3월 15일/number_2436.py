# 백준 2436
# 공약수

import sys
import math
input = sys.stdin.readline

factor = [] # 약수 리스트

gcd, lcm = map(int, input().split())

xy = lcm // gcd # 최소공배수를 최대공약수로 나눔
# x의 약수를 구해서 리스트에 저장


# x, y 구하기
for i in range(1, xy+1):
    if (xy % i == 0) and math.gcd(i, xy//i) == 1: # xy의 약수이면서 서로소(최대공약수가 1)일 때
        factor.append((i, xy//i)) # 리스트에 넣어줌

factor = factor[:len(factor)//2] # 중복 제거

minimum = factor[0][0]+factor[0][1] # 최소 담는 변수

# 두 수의 합 최소가 되는 것 찾기
for i in range(len(factor)):
    if factor[i][0]+factor[i][1] < minimum: # 반복문 돌면서 최소보다 작은게 나왔을 경우
        x = factor[i][0] # 각각의 수들을 저장해줌
        y = factor[i][1]

print(gcd* x, gcd* y)

"""
gcd ) A  B
    ----------
      x  y

      x*y가 될 수 있는 조합-그 중에서도 x, y가 서로소가 될 때를 구한 다음
      A = gcd * x, B = gcd * y이므로
      A+B = gcd*(x+y)
      따라서 x+y가 최소가 될 때의 x, y를 구한 다음에 각각 gcd를 곱해서 출력
"""



