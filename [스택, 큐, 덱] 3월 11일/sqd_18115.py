# 백준 18115
# 카드 놓기

import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 카드 n장 입력
card_skill = list(map(int, input().split())) # 길이가 n인 카드 기술 list 

card_skill.reverse() # 작업을 거꾸로 해서 처음 카드 상태를 구현해야 하므로 list reverse해주기

card = deque() # 앞뒤로 삽입하기 편하도록 deque사용

for i in range(n):
    if card_skill[i] == 1: # 1번 기술
        card.appendleft(i+1) # 카드를 제일 위에 놓음
    elif card_skill[i] == 2: # 2번 기술
        card.insert(1, i+1) # 2번째(배열로는 1번째)자리에 삽입
    else: # 3번 기술
        card.append(i+1) # 카드를 제일 밑에 내려놓음

# for i in range(n):
#     print(card[i], end=" ")
print(*card)
# *는 unpacking-리스트 괄호 벗겨줌

# 모든 작업을 거꾸로 하면 처음의 카드 순서를 알 수 있음
# 계산하기 편하도록 card_skill 순서를 거꾸로 해줌(마지막 단계가 맨 처음에 오도록)
# 마지막 단계부터(즉, reverse버전의 첫 번째 순서부터) 적혀있는 카드 기술을 거꾸로 실행해줌
"""
1. 제일 위의 카드 1장을 바닥에 내려놓는다 --> 바닥에 있는 카드를 제일 위에 둔다
2. 위에서 두 번째 카드를 바닥에 내려놓는다 --> 바닥에 있는 카드를 위에서 두 번째에 둔다
3. 제일 밑에 있는 카드를 바닥에 내려놓는다 --> 바닥에 있는 카드를 제일 밑에 둔다
"""