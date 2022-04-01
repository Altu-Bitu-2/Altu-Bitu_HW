# 백준 10971
# 외판원 순회 2
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
[외판원 순회2]
모든 도시를 방문할 수 있는 사이클을 만들고, 그 중 최소비용을 구한다.
사이클이 형성되므로 출발 도시는 중요하지 않다 -> 0으로 고정
"""

MAX = 10**8 # 최댓값 1억

# curr_city: 현재 도시의 index, left: 남은 도시의 수, cost: 현재까지의 경비
def backtracking(count, curr_city, cost):
    global answer   # 전역변수 answer 업데이트 필요
    
    if cost > answer:   # 생각해보기 : 이 조건문이 없으면 어떻게 될까요?
        return

    if count == n - 1:   # 모든 도시를 다 방문했다면 0(출발도시)으로 돌아올 수 있는지 확인
        if matrix[curr_city][0] > 0: # 출발도시로 돌아올 수 있을 때
            answer = min(answer, cost + matrix[curr_city][0]) # 둘 중에 더 작은 값 answer에 저장
        return

    for next_city in range(n): # 도시 개수만큼 반복
        if visited[next_city] or matrix[curr_city][next_city] == 0: # 방문했거나 갈 수 없는 경우
            continue # 패스
        visited[next_city] = True # 방문 체크
        backtracking(count + 1, next_city, cost + matrix[curr_city][next_city]) # count+1해주고 다시 재귀함수 부르기(다음 탐색)
        visited[next_city] = False # 다시 원래 상태로 되돌려줌

    return


# 입력
n = int(input()) # 도시 개수 입력
matrix = [list(map(int, input().split())) for _ in range(n)] # 여행 경로 입력

visited = [False] * n # 방문 체크하는 리스트 -> False로 초기화
answer = MAX # 일단 MAX로 초기화 -> 더 작은 결과가 나올 경우 갱신시켜주기

visited[0] = True # 처음은 방문 처리
backtracking(0, 0, 0)   # 0에서 출발해 n - 1개 도시를 방문
print(answer) # 결과 출력