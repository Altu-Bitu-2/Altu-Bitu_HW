# 백준 2503
# 숫자 야구
# 샘플 코드에 모든 라인에 주석 달아 추가제출 --> 나중에 다시 풀어보기!

import sys
from itertools import permutations
input = sys.stdin.readline

"""
 [숫자 야구]
 서로 다른 세 자리 수에서 위치 + 수 같으면 스트라이크, 위치는 다르고 수가 존재하면 볼
 n개의 질문으로 수와 스트라이크와 볼 개수가 주어질 때, 이를 모두 만족하는 서로 다른 세 자리 정답 수의 개수
 [풀이]
 들어오는 모든 질문에 대해, 영수의 답과 일치하지 않으면 숫자만 남긴다.
 끝까지 남아 있는 숫자가 가능한 답의 경우의 수가 된다.
"""

def count_strike_ball(s1, s2):
    # a가 답이라고 가정하고, b에 대한 스트라이크와 볼 수를 세서 리턴한다.
    strike = 0 # 스트라이크 수 세는 변수
    ball = 0 # 볼 수 세는 변수
    for i in range(3): # 이 때 s1 = 입력받은 세 자리 수, s2 = 순열로 만든 세 자리 숫자
        if s2[i] == s1[i]:  # 위치와 숫자가 모두 맞으면
            strike += 1 # strike 개수 하나 증가
        elif s2[i] in s1:   # 숫자는 있지만 위치가 다르면
            ball += 1 # ball 수 하나 증가

    return (strike, ball) # 스트라이크와 볼 수 리턴

# 영수의 답
def count_answer(questions):
    digits = [str(i) for i in range(1, 10)] # 1~9까지 list에 담음
    numbers = set(permutations(digits, 3)) # digits 안에서 3개를 뽑아 순열을 만든 후 중복 제거
    
    for s1, count in questions: # question 리스트에서 s1= 입력받는 세 자리 수, count = 영수가 말한 (strike, ball)
        temp = set()    # 주의! 여기서 temp.clear()를 쓰면 numbers가 가 같이 비워지게 됩니다.
        for s2 in numbers: # 순열 set(123~987)를 반복문으로 돌면서
            if count_strike_ball(s1, s2) == count: # 만약 스트라이크와 볼 수를 계산했을 때 count와 같다면
                temp.add(s2) # 집합에 s2를 넣음
        numbers = temp # 답이 될 수 있는 숫자 리스트를 numbers에 다시 넣음

    return len(numbers) # 영수가 생각하고 있는 답이 될 수 있는 개수

# 입력
n = int(input())
# 세자리 수는 string, 스트라이크와 볼 수는 int형으로 tuple로 묶어서 저장
initialize_input = lambda x: (x[0], (int(x[1]), int(x[2])))
# 민혁이의 질문, 스트라이크/볼 여부 -> initialize_input에서 정렬 후 question list에 넣어줌
questions = [initialize_input(input().split()) for _ in range(n)]

# 연산 + 출력
print(count_answer(questions))