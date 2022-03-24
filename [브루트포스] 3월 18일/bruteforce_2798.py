# 백준 2798
# 블랙잭

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split()) # n과 m 입력

# 입력한 카드 숫자 받기
card_list = list(map(int, input().split())) 

# 카드 중 3개 뽑아서 조합 만들기
combin = list(combinations(card_list, 3))

near = sum(combin[0]) # 근사값 받는 변수 초기화
min = abs(m-sum(combin[0])) # gap이 가장 작은 변수 초기화
for i in range(len(combin)):
    gap = abs(m-sum(combin[i])) # gap = 절댓값(m-3개 조합의 합)
    if gap < min: # 최소보다 gap이 작은게 있다면
        near=sum(combin[i]) # 근사값 다시 설정
        min=abs(m-sum(combin[i])) # 최소 gap도 다시 설정
    else:
        continue

print(near)

