# 백준 1009
# 분산처리

import sys

input = sys.stdin.readline

t = int(input()) # 테스트케이스 개수 입력

for i in range(t): # t만큼 반복
    a, b = map(int, input().split()) # a와 b 입력
    after = b % 4 # 입력받은 b를 4로 나눠서 나머지를 after에 넣음 
    if after == 0: # 만약 after가 0이면
        after = 4 # 그냥 4로 만들어줌
    result = (a ** after) % 10 # 일의 자리만 도출
    if result == 0: # 만약 일의 자리가 0이면
        print(10) # 0이 아니라 10을 출력함
    else:
        print(result) # 일의 자리 0 아니면 원래대로 출력

"""
보통 최대 4승 단위로 일의 자리가 바뀜
ex) 7^1 = 7
    7^2 = 9
    7^3 = 3
    7^4 = 1
    ...
나머지 구했을 때 결과가 0이 나올 때는 나눈 수만큼 더해주기
"""