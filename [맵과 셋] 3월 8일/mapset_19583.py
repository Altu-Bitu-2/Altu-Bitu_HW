# 백준 19583
# 싸이버개강총회

import sys

input = sys.stdin.readline

s, e, q = input().split(" ") 
# 00:00부터 23:59가 범위이므로 그냥 네 자리 정수로 만들어줌
s = int(s[:2])*100+int(s[3:]) # 시작 시간
e = int(e[:2])*100+int(e[3:]) # 끝나는 시간
q = int(q[:2])*100+int(q[3:]) # 스트리밍 끝나는 시간

attendance = dict()

time, user = input().split(" ")
# 접속 시간도 네 자리 수로 만들어줌
time = int(time[:2])*100+int(time[3:]) 
if time <= s: # 시작 시간보다 작은 경우
    attendance[user] = time # 딕셔너리에 넣어줌
# else: # 시작 시간 이후 출석
#     if e <= time <= q: # 정상적으로 퇴장 했을 경우


# 입력값 개수를 모를 때 어떻게 해야 할까요..?
# 검색해봤더니 while True 안에서 try-except를 쓰라는데 
# 이러면 저만 그런진 모르겠지만 예시 입력값을 넣을 때 제대로 안 넣어지더라구요ㅠㅠ