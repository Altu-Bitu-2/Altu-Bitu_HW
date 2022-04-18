# 백준 17281
# ⚾
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
from itertools import permutations
input = sys.stdin.readline

"""
[야구]
1. 가능한 모든 배치를 구한다.
    - 이때, 4번 타자는 항상 1번 선수(0번 인덱스)여야 함을 주의
2. 구한 배치에 대해 점수를 계산
    - out이 3번을 기록하여 이닝이 바뀔 때, 이전에 베이스에 있던 선수들을 비워주어야 함
    - 선수 인덱스를 갱신하는 과정에서 인덱스 에러가 나지 않도록 모듈러 연산 해주기
"""

# 구한 순서에 대해 점수를 계산
def calc_score(order, result):
    player = 0 # 타자
    score = 0 # 현재 점수

    # result의 한 행이 inning이 되고, 
    for inning in result:
        out = 0 # 아웃당한 선수 수
        base1 = base2 = base3 = 0 # 주자 수 전부 0으로 초기화
        while out < 3: # 쓰리아웃 전일 때
            p = inning[order[player]] # 이번 타자의 포인트
            if p == 0: # 아웃일 경우
                out += 1 # 아웃당한 선수 수 + 1
            elif p == 1: # 안타일 경우
                score += base3 # 3루 주자 score
                base3 = base2 # 2루 주자 3루로
                base2 = base1 # 1루 주자 2루로
                base1 = 1 # 1루 주자 생김
            elif p == 2: # 2루타일 경우
                score += base3 + base2 # 2루, 3루 주자 모두 score
                base3 = base1 # 1루 주자가 3루로
                base2 = 1 # 2루 주자 생김
                base1 = 0 # 1루 주자 없음
            elif p == 3: # 3루타일 경우
                score += base3 + base2 + base1 # 1루, 2루, 3루 주자 모두 score
                base3 = 1 # 3루 주자 생김
                base2 = base1 = 0 # 1루, 2루 주자 없음
            else: # 홈런일 경우
                score += base3 + base2 + base1 + 1 # 모든 주자가 홈까지 가므로 모두 score
                base3 = base2 = base1 = 0 # 1, 2, 3루 없음
            # 다음 타자로 바꿔 줌
            player = (player + 1) % 9                        

    return score # 점수 리턴


# 입력
n = int(input()) # 이닝 수
result = [list(map(int, input().split())) for _ in range(n)]    # 각 이닝별 득점결과
answer = 0 # 최대 점수 저장할 변수


# 가능한 모든 배치를 구하되, 1번타자(0번 인덱스)는 고정되어 있음을 주의
for order in permutations(range(1, 9), 8):
    order = list(order)
    order.insert(3, 0)
    # 최댓값 갱신
    answer = max(answer, calc_score(order, result))

print(answer) # 최대 점수 출력
