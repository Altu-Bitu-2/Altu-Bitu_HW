# 백준 13975
# 파일 합치기 3

import sys
import heapq # 시간 초과로 list 형태에서 최소 힙으로 자료구조 변경

input = sys.stdin.readline

t = int(input()) # 테스트케이스 개수 입력
sum = 0 # 비용의 합 초기화

for _ in range(t): # 테스트케이스 개수만큼 반복
    k = int(input()) # 소설을 구성하는 장 수(파일 개수)
    file_list = list(map(int, input().split())) # 파일들의 크기 리스트로 입력받기
    # file_list.sort()
    heapq.heapify(file_list) # 리스트를 최소 힙으로 변경
    for _ in range(k-1): # k-1번 동안 반복(2개 pop하고 pop한 값 2개 더해서 다시 push하는 방식)
        first_small = heapq.heappop(file_list) # 가장 작은 파일 pop후 변수에 저장
        second_small = heapq.heappop(file_list) # 2번째로 작은 파일 pop후 변수에 저장
        temp = first_small + second_small # 가장 작은 파일과 2번째로 작은 파일 더하기
        sum += temp # 비용에 추가하기
        heapq.heappush(file_list, temp) # 더한 값을 다시 최소 힙에 push
    print(sum) # sum(비용의 합)을 출력
    sum = 0 # 다음 testcase 계산을 위해서 sum을 다시 0으로 초기화
    


