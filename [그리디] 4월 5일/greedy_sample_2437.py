# 백준 2437
# 저울
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys

input = sys.stdin.readline

"""
[저울]

- 작은 값부터 측정 가능한지 파악해야 하므로, 오름차순으로 정렬한다.
- 현재 0부터 scope까지 모든 무게를 빠짐없이 측정가능하다고 했을 때, 새로운 무게는 scope + 1보다 작거나 같아야 한다.
- ex) 현재 1~5까지 측정 가능한데, 다음 값이 7인 경우 -> 6은 측정 불가
- 만약 이 조건을 만족할 경우, 측정 가능한 범위는 [1, scope + 새로운 무게]로 갱신된다.
- 모든 저울을 살펴봤는데도 비어있는 값이 없으면, scope + 1 리턴
"""

def find_unmeasurable(weight):
    weight.sort()   # 작은 무게부터 봐야 하므로 정렬
    scope = 0 # 측정 가능한 최대 무게

    for w in weight: # weight 리스트 요소들 반복
        if scope + 1 < w: # scope + 1 이 weight에 있는 값보다 작을 경우
            return scope + 1 # scope + 1은 측정 불가하므로 바로 리턴
        scope += w # 새로운 무게가 scope + 1 보다 작을 때 -> scope = scope + w          

    return scope + 1 # 모든 저울을 살펴봤는데 비어있는 값이 없으면, scope + 1 리턴

n = int(input()) # 저울추의 개수 n 입력
weight = list(map(int, input().split())) # 추들의 무게 리스트로 입력

print(find_unmeasurable(weight)) # 추들로 측정할 수 없는 양의 정수 중 최솟값 출력


