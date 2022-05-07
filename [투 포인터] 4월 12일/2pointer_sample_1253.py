# 백준 1253
# 좋다
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
 [좋다]
 1. 각 수마다 양 쪽 끝에서 포인터를 시작해서 좁혀오면서 어떤 '다른 두 수'가 현재 수를 만들 수 있는지 검사
 2. 포인터를 차례로 옮기며 검사하기 위해 미리 수를 오름차순 정렬함
 3. 현재 만드려는 수의 위치와 left, right 포인터 위치가 겹칠 경우 처리 주의
 4. left와 right의 초기화 주의 -> 음수가 존재하므로, 지금 검사하는 수 보다 큰 수도 포함될 수 있음
"""

# 좋은 수의 개수를 세는 함수(투 포인터)
def count_good_numbers(n, nums):
    count = 0 # count 초기화

    for i in range(n): # n만큼 반복
        p1 = 0 # p1 초기화
        p2 = n - 1 # p2 초기화

        while p1 < p2: # p1이 p2보다 작을 때마다 반복
            if p1 == i: # 만약 p1이 i와 같으면
                p1 += 1 # p1 1 증가 
                continue # 다시 반복 돌아감
            if p2 == i: # 만약 p1이 i와 같으면
                p2 -= 1 # p2 1 감소
                continue # 다시 반복 돌아감

            if nums[p1] + nums[p2] == nums[i]: # 만약 p1과 p2의 인덱스의 값의 합이 i 인덱스의 값과 동일할 경우
                count += 1 # count 1 증가
                break # 반복 멈추기
            if nums[p1] + nums[p2] < nums[i]: # 만약 p1과 p2의 인덱스의 값의 합이 i 인덱스 값보다 작다면
                p1 += 1 # p1 1 증가
            else: # 만약 nums[p1]+nums[p2] > nums[i]
                p2 -= 1 # p2 1 감소

    return count # count 리턴

# 입력
n = int(input())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬

# 연산 + 출력
print(count_good_numbers(n, nums))