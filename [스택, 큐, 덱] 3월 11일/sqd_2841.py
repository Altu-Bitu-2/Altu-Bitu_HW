# 백준 2841
# 외계인의 기타 연주

import sys

input = sys.stdin.readline

n, p = map(int, input().split())

# 6개 줄 각각 list만들어줌 -> [ [], [],...,[] ]
stack = [ [] for i in range(7)] 
count = 0 # 손가락 움직이는 횟수 count

for i in range(n): # n번 동안 입력받음
    line, fret = map(int, input().split()) # 줄 번호와 프렛 번호 입력

    ### 스택이 비어있을 경우
    if len(stack[line-1]) == 0:
        stack[line-1].append(fret) # fret push해줌
        count += 1 # count +1

    ### 스택에 원소가 있는 경우
    else: 
        if fret > stack[line-1][-1]: ### 들어오려는 프렛 > 스택 top에 있는 프렛
            stack[line-1].append(fret) # fret push
            count += 1 # count + 1
        elif fret == stack[line-1][-1]: ### 들어오려는 프렛 == 스택 top에 있는 프렛
            continue # count 세지 않고 지나가기
        ### 들어오려는 프렛 < 스택 top에 있는 프렛 (else: 이 부분 삭제해도 됨)
        # 스택이 비어있지 않은 상태에서 fret이 스택 top보다 작을 때 동안 계속 반복
        while len(stack[line-1]) != 0 and fret < stack[line-1][-1]: 
            stack[line-1].pop() # 계속 pop하고 count +1
            count += 1
        # while문을 빠져나온 상태에서 스택이 비지 않았지만 들어오려는 프렛 == 스택 top일 경우
        if len(stack[line-1]) != 0 and stack[line-1][-1] == fret: # !!!놓쳤던 부분!!! 
            # -> 그냥 count 세지 않고 지나가기
            continue
        # 위 조건에 해당하지 않을 경우(즉 pop작업이 다 끝났을 때) 드디어 push해주고 count+1
        stack[line-1].append(fret) 
        count += 1

print(count)

# 빈 스택에 새로 들어오는 경우 
#   -> push하고 count +1
# 들어오려는 프렛 > 스택 top에 있는 프렛 
#   -> push 후 그냥 count+1 (뗄 필요x)
# 들어오려는 프렛 < 스택 top에 있는 프렛
#   -> 들어오려는 프렛 숫자보다 작은 걸 발견할 때까지 스택 top부터 계속 pop, count해줌
#   -> 위 작업 해주고 나서 들어오려는 프렛 push 해주고 +1
# 들어오려는 프렛 = 스택 top에 있는 프렛
#   -> 이미 눌려진 상태이므로 count 제외