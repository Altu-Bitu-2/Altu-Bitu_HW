# 백준 20055
# 컨베이어 벨트 위에 로봇
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
from collections import deque
input = sys.stdin.readline

"""
 [컨베이어 벨트 위의 로봇 문제]
 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트 회전 방향으로 한 칸 이동할 수 있다면 이동 (이동가능: 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상이어야 함)
 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
 4. 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료. 그렇지 않다면 1로 돌아감
 [문제 풀이]
 벨트의 회전을 구현하기 위해서 deque 사용
 1번: 벨트를 오른쪽으로 한칸 회전
 2번: 가장 먼저 올라간 로봇부터 고려해야 하므로 (내리는 위치 - 1)부터 (올리는 위치)까지 검사 -> 로봇 옮기는 거 가능하면 존재여부 체크하고 내구도 감소
 3번: 올리는 위치 칸 내구도 0이 아니라면 해당 칸 로봇 존재 여부 체크 + 내구도 감소
"""

def simulation(n, k, belt):
    size = 2 * n # 컨베이어 벨트 사이즈
    robots = deque([False] * size)                 # 로봇의 존재 여부를 저장
    
    up_idx = 0  # 로봇을 올리는 위치
    down_idx = n-1  # 로봇을 내리는 위치

    step = 0
    count = 0   # 내구도가 0인 칸의 수
    
    while True:
        step += 1 # 몇 단계인지 체크

        # 1. 회전
        robots.rotate(1) # 로봇 회전
        belt.rotate(1) # 벨트 회전
        
        robots[down_idx] = False    # 로봇 내리기

        # 2. 로봇 이동
        for idx in range(down_idx-1, up_idx-1, -1): # 가장 먼저 벨트에 올라간 로봇부터이므로 down_idx부터 반복
            if robots[idx] and not robots[idx + 1] and belt[idx + 1] > 0: # 로봇이 이동할 수 있는 조건일 때, 그리고 내구도가 0이 아닐 때
                robots[idx] = False # 원래 로봇이 있던 위치 false로 해주고
                robots[idx + 1] = True # 로봇이 이동한 위치는 true로 바꿔줌
                belt[idx + 1] -= 1 # 로봇이 이동하였으므로 내구도 -1
                if belt[idx + 1] == 0: # 만약 내구도가 0이 된다면
                    count += 1 # 내구도 0의 개수 count해주기

        # 내리는 위치에 로봇이 옮겨졌다면 바로 내리기
        robots[down_idx] = False

        # 3. 로봇 올리기
        if belt[up_idx] > 0: # 올리는 위치에 있는 칸의 내구도가 0이 아니면 
            robots[up_idx] = True # 올리는 위치에 로봇을 올림
            belt[up_idx] -= 1 # 로봇을 올렸으므로 그 칸의 내구도 -1
            if belt[up_idx] == 0: # 내구도가 0이면
                count += 1 # 0인 내구도 count하기

        if count >= k: # 내구도 0인 개수가 k개보다 많으면 
            break # 반복문 나오기

    return step # 단계 수 반환

# 입력
n, k = map(int, input().split()) # 벨트 칸 수와 내구도 0 개수의 기준 입력
belt = deque(map(int, input().split()))  # 벨트의 내구도를 저장


# 연산 + 출력
print(simulation(n, k, belt))
    
