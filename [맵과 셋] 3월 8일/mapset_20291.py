# 백준 20291
# 파일 정리

import sys

input = sys.stdin.readline

number = int(input()) # 파일 개수 입력
file_dict = dict() # 딕셔너리 - key = 확장자이름, value = 해당 확장자의 개수

for i in range(number):
    name, extension = input().rstrip().split(".") # 파일 이름과 확장자 입력 (.을 기준으로 나누기)
    if extension in file_dict: # 딕셔너리 key안에 extension이 이미 있으면
        file_dict[extension] += 1 # 개수 +1
    else: # extension이 존재하지 않을 경우
        file_dict[extension] = 1 # 딕셔너리 추가


sorted_dict = dict(sorted(file_dict.items())) # 딕셔너리 정렬(key 기준)
# sorted()함수 사용시 튜플로 변환되서 dict()을 씌워줌

for key, value in sorted_dict.items(): # 결과 출력
    print(key, value)




