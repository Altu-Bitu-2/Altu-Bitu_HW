# 백준 2812
# 크게 만들기
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
[크게 만들기]
- 어차피 남는 수는 n-k자리 수!
- 가능한 앞자리에 큰 수를 배치하는 것이 유리하다.
- 수의 앞자리부터 탐색하며, 스택에 차례대로 저장
- 직전 자리보다 큰 수가 나오면 스택의 top이 자신보다 크거나 같아질 때까지 pop한 뒤에 추가
 ex) 1924 에서 2개를 지워서 큰 수를 만들어야 한다면
    stack: []           이번 숫자 '1' -> stack: ['1']
    stack: ['1']        이번 숫자 '9' -> stack: ['9']
    stack: ['9']        이번 숫자 '2' -> stack: ['9', '2']
    stack: ['9', '2']   이번 숫자 '4' -> stack: ['9', '4']
    
    답: 94
- 정확히 k개의 수를 지워야 함을 유의
"""

def find_max_number(n, k, num):
    stack = [] # 스택 리스트
    count = 0 # 지우는 횟수 k번 채우기 위한 변수

    for digit in num: # n자리 숫자 리스트 요소 반복
        # 반복 횟수가 k보다 작을 때까지, stack에 요소가 있을 동안, 그리고 스택 top이 자신보다 작을 경우
        while count < k and stack and digit > stack[-1]: 
            stack.pop() # 스택의 top이 자신보다 크거나 같아질 때까지 pop
            count += 1 # 지우는 횟수 + 1

        stack.append(digit) # 위 조건에 해당하지 않을 경우 stack에 추가
    return ''.join(stack[:n-k]) # n-k개 만큼의 숫자 문자열로 만들기

# 입력
n, k = map(int, input().split()) # 주어지는 숫자의 자리수 n, 지우는 숫자의 개수 k 입력
num = list(input().rstrip()) # n자리 숫자 입력

# 연산 + 출력
print(find_max_number(n, k, num))