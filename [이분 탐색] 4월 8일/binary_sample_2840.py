# 백준 2840
# 행운의 바퀴
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

"""
[행운의 바퀴]
- 바퀴가 돌아갈 필요 X
- 화살표가 가르키는 인덱스를 회전 정보에 따라 바꿔줌
1. 화살표가 가르키는 칸이 결정되지 않았으면 알파벳을 바퀴에 적는다.
2. 이미 알파벳이 써 있는 경우, 같은 알파벳이 아닌 경우 조건에 해당하는 바퀴 만들 수 없다.
3. 바퀴에 쓰여있는 알파벳은 중복되지 않으므로 동일한 알파벳이 여러 자리에 있을 수 없다.
"""

def make_wheel(n, record):
    wheel = ['?'] * n   # 바퀴의 상태
    is_available = dict()   # 해당 알파벳을 새로 쓸 수 있는지 확인하는 딕셔너리

    # 모든 알파벳에 대해 우선 True로 저장
    # ord(문자) = 아스키코드
    # chr(아스키코드) = 문자
    ord_a = ord('A')
    for i in range(26):
        is_available[chr(i + ord_a)] = True

    idx = 0 # 화살표가 가르키는 인덱스

    for rot, alpha in record:
        idx = (idx - int(rot)) % n # idx -> 회전할 때마다 변경
        
        # 같은 경우
        if wheel[idx] == alpha:
            continue # pass
        # 다른 알파벳이 써 있거나, 이미 알파벳을 다른 자리에 사용한 경우
        if wheel[idx] != '?' or not is_available[alpha]:
            return '!' # ! 출력
        wheel[idx] = alpha # 위 조건에 해당되지 않을 경우 wheel 리스트 idx번째에 alpha대입
        is_available[alpha] = False # 같은 alpha 사용 x (한번 사용되었으므로)
                
    return ''.join(wheel[idx:]+wheel[:idx]) # wheel 리스트 출력 (idx 원소만 빼고)

# 입력
n, k = map(int, input().split()) # 바퀴의 칸 수, 상덕이가 바퀴를 돌리는 횟수 입력
# 바퀴를 회전시켰을 때 화살표가 가리키는 글자가 몇 번 바뀌었는지, 회전을 멈추었을 때 가리키던 글자 입력
record = [input().split() for _ in range(k)]  
    
print(make_wheel(n, record)) # 결과 출력