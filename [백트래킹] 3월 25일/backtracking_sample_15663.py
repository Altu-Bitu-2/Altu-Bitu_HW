# 백준 15663
# N과 M 시리즈 (9)
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline


"""
 1. 우선 수열을 사전 순으로 증가하는 순서로 출력해야 하므로 주어진 수열을 오름차순 정렬
 2. 이 상태에서 우선, 같은 위치의 수를 또 선택하지 않도록 중복제거 (check 배열 사용)를 해줌
 3. 그 후, 중복되는 "수열"을 거르는 방법은 이전에 선택한 값을 변수에 저장해서, 수열을 만들다 다시 루트 노드로 돌아왔을 때
    이전에 선택한 값과 같은 값이면 넘어가면 됨! -> 어차피 같은 수이므로 같은 과정 반복해서 똑같은 수열이 나올 것
"""

def backtracking(idx, m):
    if idx == m: # 인덱스가 m일 때 (즉 m개를 뽑았을 때)
        print(*answer) # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
                       # print(*[1, 2, 3]) == print(1, 2, 3)
        return # 함수 중단

    prev = 0    # 이전에 선택한 값
    for i in range(n): # n번 반복
        if not checked[i] and arr[i] != prev: # 방문한 적 없고 arr[i]가 이전에 선택한 값이 아닐 때
            checked[i] = True # 방문 체크
            prev = arr[i] # arr[i]를 이전에 선택한 값으로 저장
            answer[idx] = arr[i] # arr[i]를 answer[idx]에 저장
            backtracking(idx + 1, m) # 인덱스에 +1 시킨 후 재귀함수를 부르기(다음 탐색)
            checked[i] = False # 다시 원래 상태로 되돌려줌

    return # 함수 중단
            
n, m = map(int, input().split()) # n(수의 개수)과 m(뽑는 개수) 입력
arr = list(map(int, input().split())) # n개의 수 입력
arr.sort() # 사전 순으로 증가하는 순서 -> 오름차순 정렬
checked = [False] * n # 중복 체크하는 리스트
answer = [0] * m # 출력할 수열

backtracking(0, m) # 수열 계산