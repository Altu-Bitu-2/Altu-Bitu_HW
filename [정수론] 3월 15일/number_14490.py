# 백준 11490
# 백대열

import sys
input = sys.stdin.readline

n, m = map(int, input().split(':')) # n, m 입력

# 유클리드 호제법
# n > m일 때, n과 m의 최대공약수는 n%m과 m의 최대공약수와 같음
def gcd_iter(n, m):
    big = max(n, m) # n, m 중에 큰 것
    small = min(n, m) # n, m 중에 작은 것
    while(small): # min(n, m)이 0일 때, max(n, m)이 최대공약수
        big %= small # max(n, m) = max(n, m) % min(n, m)
        big, small = small, big # big, small swap
    return big # m이 0일 때, n의 값이 최대공약수

gcd = gcd_iter(n, m) # gcd = n과 m의 최대공약수
print("{0}:{1}".format(n//gcd, m//gcd))

# 약분할 때는 두 수의 최대공약수로 나눠주기