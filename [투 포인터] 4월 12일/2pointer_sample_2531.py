# 백준 2531
# 회전 초밥
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 [회전 초밥]
 1. 연속해서 먹어야 할 접시가 k로 고정됐기 때문에 슬라이딩 윈도우
 2. 직선이 아니라 원 형태의 배열! 모듈러 연산을 통해 윈도우의 양 끝 위치 조절하기
 3. 쿠폰으로 먹은 초밥을 먼저 고려해놓기
 4. 초밥의 종류가 최대 3000개로 많지 않음. 각 종류별 먹은 초밥의 개수를 세어주기
"""

def choose_sushi(n, d, k, c, belt):
    sushi = [0]*(d+1)   # 각 인덱스의 초밥 개수

    # 쿠폰으로 먹게 되는 초밥
    sushi[c] = 1
    count = 1

    # 윈도우 초기화
    for i in range(k): # 연속해서 먹어야 할 접시 개수만큼 반복
        if sushi[belt[i]] == 0: # 만약 i번째 접시에 있는 초밥의 값이 0일 경우
            count += 1 # count 1 증가
        sushi[belt[i]] += 1 # i번째 접시에 있는 초밥의 값 1 증가

    ans = count # ans = count

    # 슬라이딩 윈도우
    for idx in range(k, n+k): # 슬라이딩 윈도우
        sushi[belt[idx - k]] -= 1 # 1개씩 먹음
        if sushi[belt[idx - k]] == 0: # 만약 값이 0이면
            count -= 1 # count 1 감소
        
        if sushi[belt[idx % n]] == 0: # 만약 값이 0이면
            count += 1 # count 1 증가
        sushi[belt[idx % n]] += 1 # 스시 한 개씩 추가
        
        ans = max(ans, count) # 결과는 위의 ans과 count 중 큰 것

    return ans # ans 리턴

# 입력
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
# 연산 + 출력
print(choose_sushi(n, d, k, c, belt))