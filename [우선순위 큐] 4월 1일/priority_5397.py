# 백준 5397
# 키로거

import sys
from collections import deque

"""
left 리스트와 right 리스트 사이에 입력(커서)이 있는 방식
[ left ] 커서 [ right ]
< : left 맨 뒤 요소 -> right 맨 앞으로 이동
> : right 맨 앞 요소 -> left 맨 뒤로 이동
- : left 맨 뒤 요소 삭제
기타 알파벳/숫자 : 그냥 left에 append

"""

input = sys.stdin.readline
left = [] # 커서 앞 리스트
right = deque() # 커서 뒤 -> 시간 초과로 deque로 변경

num = int(input()) # 테스트케이스 개수 입력

# 패스워드 만드는 함수
def make_password(testcase):
    for i in range(len(testcase)): # testcase 길이만큼 반복
        if testcase[i] == '<': # 커서를 왼쪽으로 움직일 때
            if len(left) == 0: # left 배열이 없는 경우
                continue       # indexError가 생기므로 패스
            right.appendleft(left[-1]) # left배열의 맨 뒤 요소를 right배열 맨 앞에 추가
            left.pop(-1) # 이동(복사) 후 해당 요소 삭제

        elif testcase[i] == '>': # 커서를 오른쪽으로 움직일 때
            if len(right) == 0: # right 배열이 없는 경우
                continue # indexError가 생기므로 패스
            left.append(right[0]) # right배열의 맨 앞 요소를 left배열 맨 뒤에 추가
            right.popleft() # 이동(복사) 후 해당 요소 삭제

        elif testcase[i] == '-': # 백스페이스키 입력
            if len(left) == 0: # 앞에 지울 문자가 없는 경우
                continue # pass
            left.pop(-1) # left 배열 맨 뒤 요소 삭제

        else: # 그냥 알파벳일 경우
            left.append(testcase[i]) # 그냥 left 배열 맨 뒤에 추가
    return [*left, *list(right)]

for i in range(num): # 입력 개수만큼 반복
    testcase = list(input().rstrip()) # testcase 입력
    password = make_password(testcase) # 패스워드 만들기
    print(''.join(password)) # 리스트를 문자열로 변환 후 출력
    # 다음 패스워드 작업을 위해 left, right 배열 clear시켜줌
    left.clear() 
    right.clear()

    