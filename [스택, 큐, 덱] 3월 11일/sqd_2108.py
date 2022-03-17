# 백준 2108
# 통계학

import sys

input = sys.stdin.readline

number = int(input()) # 수의 개수 (홀수)

n_list = [] # 수들을 저장하는 리스트

# 수들을 리스트에 넣어줌
for i in range(number):
    x = int(input())
    n_list.append(x)

sum = 0 # 수들의 합을 저장할 변수

####산술평균 출력####
for i in range(number):
    sum += n_list[i] # n개의 수들을 모두 더함
print(round(sum/number)) # n개의 수들의 합을 n으로 나눔

####중앙값 출력####
n_list.sort() # 오름차순으로 정렬
# 중앙값 : 1~5까지 있을 때 5 // 2 + 1 
# list는 index가 0부터 시작하므로 위 식에 -1
print(n_list[(number-1)//2]) 

####최빈값 출력####
n_dict=dict() # 수와 수들이 입력된 횟수 저장하는 딕셔너리
for i in range(len(n_list)):
    if n_list[i] not in n_dict: # 딕셔너리에 수가 없으면
        n_dict[n_list[i]] = 1 # value = 1
    else: # 딕셔너리에 수가 이미 있으면
        n_dict[n_list[i]] += 1 # +1
# n_dict()를 value기준으로 내림차순 정렬, value가 같을 경우 key순으로 오름차순 정렬
sorted_dict = sorted(n_dict.items(), key = lambda x: (-x[1], x[0]))

if number > 1: # 수의 개수가 1개가 넘으면
    if sorted_dict[0][1] == sorted_dict[1][1]: # 최빈값이 2개 이상일 경우
        print(sorted_dict[1][0]) # 두 번째로 작은 값 출력
    else: # 최빈값이 하나일 경우
        print(sorted_dict[0][0]) # 해당 최빈값 출력
else: # 수의 개수가 1개만 있을 때
    print(sorted_dict[0][0])

####범위 출력####
print(n_list[number-1] - n_list[0])