# 백준 20920
# 영단어 암기는 괴로워

import sys

input = sys.stdin.readline

number, min_length = map(int, input().split())

word_dict= dict()

for i in range(number):
    word = input().rstrip() # 단어 입력
    if len(word) < min_length:
        continue
    else:
        if word in word_dict: # 딕셔너리 key안에 단어가 이미 있으면
            word_dict[word] += 1 # 개수 +1
        else: # 단어가 존재하지 않을 경우
            word_dict[word] = 1 # 딕셔너리 추가


result = sorted(word_dict.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(result)):
    print(result[i][0])