# 백준 9084
# 동전
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 dp[i] = 주어진 동전 종류를 사용해서 i원을 만드는 경우의 수
 dp[0] = 1 을 넣고 시작 (0원을 만드는 경우의 수 1로 생각)
 각 동전마다 해당 동전부터 만들어야 하는 금액(m)까지 돌리면서 해당 동전을 사용하기 전 금액의 경우의 수와 현재 경우의 수를 더함
 !주의! 이때, 해당 동전 사용하기 전 금액의 경우의 수가 0이면 금액을 만들 수 없는 경우이므로 더하면 안됨
"""

MAX = 10**4 # 최댓값

def count(n, m, coin):
    dp = [0] * (m+1) # [0, 0, ... , 0 (총 m+1개)]
    dp[0] = 1 # 초기 세팅

    for c in coin: # N가지 동전의 각 금액 리스트 요소 반복
        for idx in range(c, m+1): # c~m+1 까지
            dp[idx] += dp[idx - c] # 해당 동전 사용하기 전 금액의 경우의 수와 현재 경우의 수 더하기

    return dp[m] # 만들어야 하는 금액 리턴

# 입력
t = int(input()) # 테스트케이스 개수 입력

for _ in range(t):
    # 입력
    n = int(input()) # 동전의 가지 수 
    coin = list(map(int, input().split())) # N가지 동전의 각 금액
    m = int(input()) # 동전으로 만들어야 할 금액
    # 연산 + 출력
    print(count(n, m, coin))