# 백준 11057
# 오르막 수

import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n)]

for i in range(10):
    dp[0][i] = 1
    
print(dp)