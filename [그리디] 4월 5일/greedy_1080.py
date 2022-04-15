# 백준 1080
# 행렬

import sys

input = sys.stdin.readline

count = 0

n, m = map(int, input().split())

# 0->1, 1->0 바꿔주는 함수
def change_number(matrix1, i, j):
    for x in range(i, i+3): # 전달받은 i, j위치부터 3x3 크기만큼 변환해주기
        for y in range(j, j+3):
            matrix1[x][y] = 1 - matrix1[x][y]

# 행렬 A 입력
matrix1 = [list(map(int, input().rstrip())) for _ in range(n)]

# 행렬 B 입력
matrix2 = [list(map(int, input().rstrip())) for _ in range(n)]

# 만약 행렬 A와 행렬 B가 다른 지점이 있으면 count+1을 해주고 flip해줌
for i in range(n-2): # 3x3 크기이므로 마지막 반복 index 지점은 n-2가 되어야 함
    for j in range(m-2): # 3x3 크기이므로 마지막 반복 index지점은 m-2가 되어야 함
        if matrix1[i][j] != matrix2[i][j]: # 만약 같지 않으면
            count += 1 # 변환 횟수 +1
            change_number(matrix1, i, j) # flip해줌

same = True # 두 행렬이 같은지 아닌지 확인

# 행렬 전체 돌면서 두 행렬이 다른 지점이 있을 경우 False로 바꿔줌
for i in range(0, n):
    for j in range(0, m):
        if matrix1[i][j] != matrix2[i][j]: # 만약 두 행렬이 다를 경우
            same = False # 같지 않다(False)로 바꿔주기
            break # 다른 지점을 발견했을 경우 즉시 break

if same == False: # 만약 같지 않으면 (즉, 행렬 A를 행렬 B로 변환할 수 없으면)
    print(-1)
else: # 만약 같으면 (변환할 수 있는 경우)
    print(count)


