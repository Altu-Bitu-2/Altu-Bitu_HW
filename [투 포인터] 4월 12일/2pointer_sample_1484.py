# 백준 1484
# 다이어트
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 [다이어트]
 left: 성원이가 기억하고 있던 몸무게
 right: 성원이의 현재 몸무게
 같은 위치에서 시작해서 점점 증가하는 투 포인터로 풀이
 대신, left ~ right를 모두 고려하는 것이 아니라 left, right 포인터 값 자체만 고려
 !주의! 몸무게의 범위가 딱히 정해져 있지 않으므로, 종료 조건을 잘 세우는 것이 중요!
       -> 두 몸무게가 같아지는 순간 종료!
       -> left가 right와 같은 값을 가진다면, 직전 상황은 두 몸무게가 1차이 나는 상황
       -> 이 때 몸무게 차이가 g 이상이었다는 것은 이후로 나올 수 있는 차이는 무조건 g 이상이 된다. (제곱수의 간격은 수가 커질 수록 늘어나기 때문)
"""

def get_possible_weight(g):
    left = 1 # 성원이가 기억하고 있던 몸무게 초기화
    right = 2 # 성원이의 현재 몸무게 초기화
    ans = [] # ans 리스트 
    while left < right: # right가 더 클 경우 반복
        diff = right ** 2 - left ** 2 # diff = right^2 - left^2
        if diff > g: # 만약 diff가 g보다 클 경우
            left += 1 # left 1 증가
        else: # 만약 diff가 g보다 작거나 같을 경우
            if diff == g: # 만약 diff와 g가 같을 경우
                ans.append(right) # ans리스트에 right값 추가
            right += 1 # if diff != g -> right 1 증가
    return ans # ans 리스트 리턴

# 입력
g = int(input())

# 연산
ans = get_possible_weight(g)

# 출력
if ans:
    print(*ans, sep='\n')
else:
    print(-1)