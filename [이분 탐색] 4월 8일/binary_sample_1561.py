# 백준 1561
# 놀이 공원
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 [놀이 공원]
 n번째 아이가 놀이기구를 타는 시간을 구한 후, 해당 시간에 놀이기구를 타는 아이들을 모두 검사하며 n번째 아이가 타는 놀이기구의 번호를 구한다!
 1. n번째 아이가 놀이기구를 타는 시간이 언제인지 parametric search 통해 구함
    - 이때, 각 시간 별 놀이기구 타는 아이의 마지막 번호 구하는 공식은 다음과 같음
      f(t) = (모든 i(놀이 기구)에 대해서) t/num[i] + n(시간 0일때 놀이기구 타는 아이 수)
    - left: 놀이기구 타는 시간의 최소 = 0
    - right: 놀이기구 타는 시간의 최대 = n(사람 수) * (운행시간)
                                    - 여기서 운행시간은 엄밀히 말하면 주어진 운행시간 중 최솟값으로 계산해야 tight한 범위가 나오지만, 그보다 큰 값을 right로 설정해도 답이 구간 내에 존재하므로 이분탐색으로 충분히 찾을 수 있다. 따라서 이 풀이에서는 첫번째 놀이기구의 운행시간으로 계산하였다.
    - n번째 아이가 놀이기구를 타는 첫 시간을 구해야 하므로 lower bound
 2. n번째 아이가 놀이기구를 타는 시간을 구했다면, 그 시간에 마지막으로 놀이기구를 타는 아이부터 시작해서 놀이기구를 m-1부터 탐색하면서 n번째 아이가 몇 번 놀이기구 타는지 구하면 됨!
"""

# 사람 수 계산하는 함수
def calc_people(time, rides):
    people = 0 # 사람 수 저장할 변수 초기화
    for t in rides: # 놀이기구 시간 순회하며
        people += time // t + 1 # 주어진 시간 // 놀이기구 운행시간 +1 한 뒤 사람 수에 더해줌
    return people # 사람 수 리턴

# 이분 탐색하는 함수
def binary_search(n, rides):
    left = 0 # 놀이기구 타는 시간 최소
    right = rides[0] * n # 놀이기구 타는 시간 최대 (운행 시간 * 사람 수)

    while left <= right: # left가 right보다 작거나 같을 경우
        mid = (left + right) // 2 # mid 계산
        if calc_people(mid, rides) >= n: # 사람 수가 n보다 크거나 같으면
            right = mid - 1 # 최댓값 줄이기 위해서 right = mid - 1
        else: # 사람 수가 n보다 작으면
            left = mid + 1 # 최솟값 늘리기 위해서 left = mid + 1

    return left

# 마지막 아이가 타게 되는 놀이기구 번호 구하는 함수
def find_ride(n, m, rides):
    time = binary_search(n, rides) # n번째 아이가 놀이기구 타는 첫 시간
    people = calc_people(time, rides) # 사람 수 계산
    for i in range(m - 1, -1, -1): # 거꾸로 순회
        if time % rides[i] == 0: # 만약 time 시간에 탑승했고
            if people == n: # 사람 수도 n이라면
                return i + 1 # i+1 리턴
            people -= 1 # 사람 수 n이 아니면 -1

# 입력
n, m = map(int, input().split()) # 아이들 수, 놀이기구 종류 입력
rides = list(map(int, input().split())) # 놀이기구 운행 시간 입력
print(find_ride(n, m, rides)) # 마지막 아이가 타게 되는 놀이기구 번호 출력