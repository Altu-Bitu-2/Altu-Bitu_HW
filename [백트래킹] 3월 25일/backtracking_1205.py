# 백준 1205
# 등수 구하기

import sys

input = sys.stdin.readline

# 점수의 개수, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수의 개수
n, new_score, p = map(int, input().split())

if n == 0: # 입력받는 점수들의 개수가 0일 때
    print(1) # 어차피 리스트 안에 아무것도 없기 때문에 아무 점수나 넣어도 1등
else:
    scores = list(map(int, input().split())) # 점수들 리스트 입력
    scores.append(new_score) # 리스트에 태수의 새로운 점수 추가
    scores.sort(reverse=True) # 비오름차순으로 정렬

    # new_score의 index 찾기 (첫 index 찾고 count-1 만큼 더해줌)
    # (new_score에 해당하는 점수가 여러 개 있을 경우) 맨 마지막 index로 계산해야 하므로
    find_new_index = scores.index(new_score) + (scores.count(new_score) - 1)

    if find_new_index >= p: # 찾은 index가 p보다 같거나 클 경우
        print(-1) # 제한된 배열 위치를 넘어선 것이므로 -1 출력
    else: # 제한된 리스트 안에 있으면
        print(scores.index(new_score)+1) # 찾아준 index에 +1 출력 (index 0부터 시작)
