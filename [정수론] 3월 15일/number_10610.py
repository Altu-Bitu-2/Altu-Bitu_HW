# 백준 10610
# 30

import sys
input = sys.stdin.readline
 
n = int(input()) # n 입력
str_int = str(n) # n을 문자열로 바꿔주기
n_list = list(str_int) # 정렬 위해서 문자열로 바꿔준 n을 list로 바꿔주기

# 30의 배수 => 3의 배수 & 10의 배수 모두 충족해야 함
# 30의 배수를 만들기 위해서는 
# 1. n에 포함된 숫자들의 합을 3으로 나눴을 때 나머지가 0이어야 함(3의 배수) 
# 2. 마지막에 '0'으로 끝나야 하므로(10의 배수), n에 포함된 숫자 중 0이 존재해야 함

sum = 0 # n에 포함된 숫자들의 합
for i in range(len(n_list)):
    n_list[i] = int(n_list[i]) # list안의 요소들을 정수로 바꿔줌
    sum += n_list[i] # sum변수에 요소들을 모두 더함

# 요소의 합을 3으로 나눈 나머지가 0일 때 & 문자열 안에 0이 없지 않을 때(-1이면 없는 것)
if sum % 3 == 0 and str_int.find('0') != -1: 
    n_list.sort(reverse=True) # 내림차순 정렬
    for i in range(len(n_list)):
        print(n_list[i], end="")
else:
    print("-1") # 없을 경우 -1 출력 후 exit
    exit()



