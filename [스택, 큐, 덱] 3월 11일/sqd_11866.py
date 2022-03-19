# 백준 11866
# 요세푸스 문제 0

import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # n, k 입력
pointer = 0 # 포인터 역할, 초기값 0

# circle_queue에 1부터 n까지 삽입
circle_queue = list(range(1, n+1))
final_list = [] 


for i in range(n): # n번 동안 반복
    pointer = (pointer - 1 + k) % len(circle_queue)
    # 계산된 pointer를 index에 넣어주고, 그 index에 해당하는 값을 다른 list에 append해줌
    final_list.append(str(circle_queue[pointer])) 
    del circle_queue[pointer] # 넣어줬으면 해당 index 삭제

print("<"+", ".join(final_list)+">")
    

# 현재 index에서 -1을 해주고 (왜냐면 배열은 0부터 시작하니까), 그 다음에 +k를 해주기
# 원 형태이므로, 위에서 계산한 값 % 배열 크기
# 현재 pointer에 해당하는 index 삭제
#   pointer에 해당하는 index 삭제해주면, pointer가 가리키는 index는 다음 칸이 되어버리므로..
#   위에 패턴을 반복해주면 됨







