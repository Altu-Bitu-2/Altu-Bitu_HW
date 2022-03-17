# 백준 1213
# 팰린드롬 만들기

import sys

input = sys.stdin.readline

name = input().rstrip() # 임한수의 영어 이름 입력

char_dict = dict() # 문자와 문자의 개수를 저장할 딕셔너리

### 딕셔너리에 문자와 문자가 입력된 갯수 넣기 ###
for i in range(len(name)):
    if name[i] not in char_dict: # 딕셔너리에 문자가 없으면
        char_dict[name[i]] = 1 # value = 1
    else: # 딕셔너리에 문자가 이미 있으면
        char_dict[name[i]] += 1 # +1


count = 0 # value가 홀수인 알파벳 체크
odd_char='' # value가 홀수인 알파벳
total_char='' # 앞뒤로 정렬할 알파벳 string

### value가 홀수인 알파벳 수 체크 & 정렬할 알파벳만 골라내기 ###
for key, value in char_dict.items():
    if value % 2 == 0: # value가 짝수일 경우
        total_char += (key * (value // 2)) # total_char에 해당 key를 value의 반만큼 곱해서 넣어줌
        # 예를 들어 value가 4일 경우 total_char에 2만큼 넣어줌
    else: # value가 홀수일 경우
        count += 1 # count++
        odd_char=key # value가 홀수인 문자에 추가
        if value >= 3: # value가 홀수인 문자 중에서 횟수가 3 이상일 경우
            total_char += (key * (value // 2))
            # 예를 들어 value가 5일 경우 total_char에 2만큼 넣어줌

### 최종 문자열 정렬해주는 함수 ###
def make_palin(odd_char, total_char, count):
    sorted_string = ''.join(sorted(total_char)) # total_char을 정렬
        # 이 때 sorted함수는 리스트로 변환해서 정렬하므로 다시 join시켜줌
    if count == 1: # value가 홀수인 수가 1개일 때
        print(sorted_string+odd_char+sorted_string[::-1]) 
        # 정렬된 문자열과 value가 홀수인 알파벳, reverse된 문자열 출력
    else:
        # 모든 알파벳이 짝수 개수로 입력됐을 때
        print(sorted_string+sorted_string[::-1]) # 정렬된 문자열과 reverse된 문자열 출력

if count > 1: # value가 홀수인 수가 2개 이상이면 --> 팰린드롬x
    print("I'm Sorry Hansoo") 
else: # value가 홀수인 수가 1개 이하일 경우 --> 팰린드롬
    make_palin(odd_char, total_char, count)


# dict()을 사용해서 key = 문자, value = 문자의 개수 저장
# 팰린드론의 조건 :
#   들어오는 모든 문자가 짝수 개일 때
#   한 종류의 문자만 홀수 개이고, 나머지 문자들은 짝수 개
