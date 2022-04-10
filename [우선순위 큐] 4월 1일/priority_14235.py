# 백준 14235
# 크리스마스 선물

import sys
import heapq as hq

input = sys.stdin.readline

heap = [] # heap으로 사용할 리스트

n = int(input()) # n 입력
for i in range(n): # n번 반복
    a = list(map(int, input().split())) # 값이 몇 개가 들어올지 모르니 a를 리스트로 입력
    if a[0] == 0: # 입력값이 0인 경우
        if len(heap) == 0: # 줄 선물이 없을 경우
            print(-1) # -1 출력
        else: # 줄 선물이 있는 경우
            present = hq.heappop(heap) # top(가장 최소값) 삭제 후 반환
            print(-present) # -붙여서 삽입했었기 때문에 -붙여서 출력
    else:
        for i in range(1, len(a)):
            hq.heappush(heap, -a[i]) 
            # 파이썬 heapq-> 최소 힙
            # 일단 - 붙여서 삽입하고 출력 시 다시 - 붙여서 출력

        