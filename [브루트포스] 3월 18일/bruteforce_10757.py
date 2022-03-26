# 백준 10757
# 큰 수 A+B

import sys

input = sys.stdin.readline

a, b = input().split() # 일단 문자열로 받기
list_x=[] # 길이가 더 큰 문자열을 받는 리스트 (피가산수)
list_y=[] # 길이가 더 작은 문자열을 받는 리스트

if len(a) >= len(b): # 문자열 a의 길이가 b의 길이보다 크거나 같을 경우
    list_x = list(a)
    list_y = list(b)
else: # 문자열 b의 길이가 더 클 경우
    list_x = list(b)
    list_y = list(a)

# 계산하기 편하게 reverse해줌
list_x.reverse()
list_y.reverse()

# 두 리스트 길이 동일하게 만들어주기 위해서 길이가 더 작은 리스트에 0 추가
for i in range(len(list_x)-len(list_y)):
    list_y.append('0')

# 리스트 안의 요소들 int로 바꿔주기
list_x = [int(i) for i in list_x] 
list_y = [int(i) for i in list_y]

for i in range(len(list_x)-1): # a, b 중 길이가 작은 횟수 만큼
    if list_x[i]+list_y[i] < 10: # index끼리의 합이 10이 넘지 않는 경우
        list_x[i] += list_y[i] # x, y 그냥 더해줌
    else: # 10이 넘어가는 경우
        one = (list_x[i]+list_y[i]) % 10 # 일의 자리만 따로 계산
        list_x[i] = one # 일의 자리만 넣어줌
        list_x[i+1] += 1 # index 한 칸 뒤에 +1 해줌

# 맨 마지막 index 계산
if list_x[-1]+list_y[-1] < 10: # 10이 넘지 않는 경우
    list_x[-1] += list_y[-1] # 원래대로 계산
else: # 10이 넘는 경우
    one = (list_x[-1]+list_y[-1]) % 10
    list_x[-1] = one
    list_x.append(1) # !!index 한칸 더 추가한 다음!! +1 해주기


# 다시 원래대로 순서 복구
list_x.reverse()

for i in range(len(list_x)): # 출력
    print(list_x[i], end="")

"""
자리수 맞춰서 계산하기
1) 만약 자리수끼리 더했는데 10이 넘는다 -> 일의 자리만 계산하고 다음 index에 +1
2) 제일 큰 자리수의 합이 10이 넘는다 -> 리스트 index 하나 더 추가하고 그곳에 +1
3) 리스트 요소들 공백없이 합쳐서 출력
"""



