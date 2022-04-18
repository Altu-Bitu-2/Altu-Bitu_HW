# 백준 2805
# 나무 자르기
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 [나무 자르기]
 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?
 -> 절단기의 높이가 k(임의의 값)일 때, M미터의 나무를 집에 가져갈 수 있는가?
 left: 절단기의 최소 높이 -> 0
 right: 절단기의 최대 높이 -> 주어진 나무 중 가장 높은 나무 높이
"""

# 내림차순으로 정렬된 리스트에서 height보다 값이 큰 요소들에 대해 각 길이와 height의 차를 모두 더해서 리턴
def cut_tree(height, tree):
    total = 0

    for h in tree: # tree들 리스트 요소들 반복
        if h <= height: # tree 리스트 요소가 height보다 높거나 같을 경우
            return total # total return
        total += h - height # 위 조건이 아닐 경우 h - height값을 total에 더해줌
    
    return total # total return

# 이분 탐색 함수
def binary_search(target, tree):
    left = 1 # left = 절단기의 최소 높이
    right = tree[0] # right = 절단기의 최대 높이

    while left <= right: # left가 right보다 작거나 같을 경우
        mid = (left + right) // 2 # mid값 구하기
        if cut_tree(mid, tree) >= target: # cut_tree결과값이 target보다 크거나 같을 경우
            left = mid + 1 # left값에 mid + 1 대입
        else: # cut_tree값이 target보다 작을 경우
            right = mid - 1 # right값에 mid - 1 대입

    return left - 1 # left - 1 return

# 입력
n, m = map(int, input().split()) # 나무 수와 상근이가 집으로 가져가려고 하는 나무의 길이 입력 
tree = list(map(int, input().split())) # 나무의 높이들 입력
tree.sort(reverse=True) # 내림차순 정렬
print(binary_search(m, tree)) # 답 출력