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

sum_set = set() # 각 조합들의 합을 모아놓는 set(중복 제거 위해서 집합 자료형)
for i in range(len(combin)):
    if m-sum(combin[i]) < 0: # !! 한 조합의 합이 m보다 크면 조건에 부합하지 x !!
        continue # 그냥 패스시켜줌
    elif m - sum(combin[0]) == 0: # m과 똑같은 숫자가 있으면
        print(sum(combin[i])) # 출력 후 바로 프로그램 종료
        exit()
    else: # 한 조합의 합이 m보다 작은 경우 -> set에 add시켜줌
        sum_set.add(sum(combin[i]))

# 코드가 여기까지 왔다면 m과 같은 숫자 없이 m보다 작은 숫자만 있을 것임
sum_list = list(sum_set) # 집합을 리스트로 변경
sum_list.sort() # 오름차순 정렬
print(sum_list[-1]) # m보다 작으면서 m과 가장 가까운 수 -> 맨 마지막 index


