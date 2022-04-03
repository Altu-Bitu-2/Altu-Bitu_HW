# 백준 11053
# 가장 긴 증가하는 부분 수열

import sys

input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))

dp = [1] * n # dp 리스트 1로 초기화

for i in range(n): # 수열 길이만큼 반복
    for j in range(i): # 0 ~ i-1번까지 탐색
        if a_list[i] > a_list[j]: # 만약 i번째 값이 i번째 이전 값들보다 클 때
            dp[i] = max(dp[i], dp[j]+1) # 현재 dp[i]자신과 dp[반복문 돌고 있는 i 이전 index]+1 값 중에 더 큰 값 선택

print(max(dp)) # 최대 길이 출력

