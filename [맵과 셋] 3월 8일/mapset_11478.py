# 백준 11478
# 서로 다른 부분 문자열의 개수

import sys

input = sys.stdin.readline

string = input().rstrip() # 문자열 입력

s_list = [] # 부분 문자열들 담아놓는 리스트

for i in range(len(string)): # i = 0, 1, ..., string길이-1
    for j in range(len(string)-i): # string 길이의 반비례 - i가 2일 때 j= 0, 1, ..., (string길이-2)-1
        s_list.append(string[i:i+j+1]) 

# print(s_list)
s_set = set(s_list) # set()에 넣어 중복 제거
# print(s_set)
print(len(s_set)) # 집합의 길이(즉, 중복되지 않은 부분 문자열의 개수) 출력