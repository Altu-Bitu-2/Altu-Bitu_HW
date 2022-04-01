# 백준 14888
# 연산자 끼워넣기
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
sys.stdin.readline

"""
[연산자 끼워넣기]
연산자를 모두 돌려보면서 배치한 후, 각 연산자에 따른 값 계산
"""

MAX = 10**9 # 최대값 10억

add = lambda x, y: x + y # 더하기 함수
sub = lambda x, y: x - y # 빼기 함수
multiply = lambda x, y: x * y # 곱하기 함수

# C++14 방식에 맞추어 나누기 함수 작성
def division(x, y): 
    if x < 0: # x가 음수일 경우
        return - (-x // y) # 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿔줌
    return x // y # 정수 나눗셈 return

# 인덱스에 맞는 연산을 하기 위해 함수를 리스트에 저장
functions = [add, sub, multiply, division]

# cnt: 수 인덱스, value: 현재까지 연산 결과
def backtracking(cnt, value):
    global max_value, min_value # 만들 수 있는 식의 결과의 최댓값/최소값 -> 전역변수로 설정
    if cnt == n:    # 연산이 모두 완료 되었다면
        max_value = max(max_value, value) # 만들 수 있는 식 결과 최댓값과 현재까지 연산 결과 중에 더 큰 것
        min_value = min(min_value, value) # 만들 수 있는 식 결과 최솟값과 현재까지 연산 결과 중에 더 작은 것
        return # 중단

    for i in range(4): # operator 리스트 크기만큼 반복(4) 
        if operator[i] > 0: # 연산자의 개수가 있으면
            operator[i] -= 1 # 연산자의 개수 미리 하나 줄여주고
            backtracking(cnt + 1, functions[i](value, numbers[cnt]))    # i번째 함수에 value와 numbers[cnt]를 인자로 넘겨주어 계산함
            operator[i] += 1 # 연산자의 개수 다시 복구시켜줌
    return

# 입력
n = int(input()) # 수의 개수 입력
numbers = list(map(int, input().split())) # a1~an까지 입력
operator = list(map(int, input().split())) # 각각 +-*/ 개수

max_value = -MAX   # 현재까지 최대값 기록
min_value = MAX    # 현재까지 최솟값 기록

# 연산
backtracking(1, numbers[0])
# 출력
print(max_value, min_value, sep='\n')