# 백준 12840
# 창용이의 시계

import sys

input = sys.stdin.readline

h, m, s = map(int, input().split()) # 현재 시간 입력
q_num = int(input()) # 쿼리의 개수 입력
DAY = 86400 # 하루는 86400초

total = h * 3600 + m * 60 + s # 입력받은 시간은 초로 환산

for i in range(q_num):
    q = list(map(int, input().split())) # t와 c 입력 (c가 필요없는 경우 대비하여 리스트로 입력받음)
    # 이 때 q[0]은 t, q[1]은 c
    if q[0] == 1: # t가 1일 때 -> c초만큼 앞으로 돌리기
        total = (total + q[1]) % DAY
    elif q[0] == 2:# t가 2일 때 -> c초만큼 뒤로 돌리기
        total = (total - q[1]) % DAY
        if q[1] < 0: # 만약 total에서 c초를 뺐는데 음수가 나왔다면
            q[1] += DAY # 하루(86400초)를 더해줌

    else:
        # t가 3일 때 - > 현재 시간 print
        hour = total // 60 // 60
        minute = (total // 60) % 60
        second = total % 60
        print(hour, minute, second)

        



