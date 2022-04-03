# 백준 1316
# 그룹 단어 체커

import sys

input = sys.stdin.readline

n = int(input()) # 단어 개수 입력
group_word = [] # word들 담아놓는 리스트
# 연속된 문자만 뺀 상태의 문자열을 담아두는 용도의 리스트
stack = [[] for _ in range(n)] # 단어 개수만큼 리스트안에 리스트를 넣어주기

# word들 입력받기
for i in range(n):
    group_word.append(input().rstrip()) 

# 문자열에서 연속된 문자만 빼서 리스트에 담아둠
for i in range(len(group_word)):
    stack[i].append(group_word[i][0]) # 문자열에서 첫 번째 문자는 일단 stack에 담아둠
    for j in range(1, len(group_word[i])): # index 1 ~ 끝까지
        if group_word[i][j] == group_word[i][j-1]: # 현재 index(문자)가 이전 index와 같을 때
            continue # stack리스트에 담아두지 않고 pass
        else: # 현재 index != 이전 index
            stack[i].append(group_word[i][j]) # 현재 index를 stack 해당 위치의 리스트에 담아둠

count = 0 # 그룹 단어 체크하는 변수

# stack[0]~stack[-1]에서 중복된 문자가 있는지 확인하기
for i in range(len(stack)):
    if len(stack[i]) != len(set(stack[i])): # 중복 있으면
        continue # count 하지 않음
    else: # 중복 없으면
        count += 1 # count +1 해줌

print(count) # 결과 출력
        

"""
index 0은 일단 리스트에 담아두고
index 1부터 비교 시작해서
현재 index가 이전 index와 다른 문자다 -> 현재 index를 stack에 담아둠
같은 문자다 -> pass

stack에서 리스트 안에 중복된 요소가 있으면 count 하지x
리스트 안에 각자 다른 문자들만 있으면 count +1
"""
