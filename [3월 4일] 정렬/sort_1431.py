# 백준 1431
# 시리얼 번호

import sys

input = sys.stdin.readline

serial_num = [] # 시리얼 번호 모아놓은 리스트

number = int(input()) # 기타의 개수

for i in range(number):
    a = input().rstrip()
    serial_num.append(a) # 문자열 리스트에 저장



def pick_number(x):
    sum = 0
    for i in x:
        # print(i)
        if i.isdigit() == True:
            sum += int(i)
        else:
            sum += 0
    return sum

serial_num.sort(key=lambda x:(len(x), pick_number(x), x))

for i in serial_num:
    print(i)

# 얼떨결에 성공시키긴 한 것 같은데 왜 이게 실행이 되는지 궁금합니다
# lambda 함수에서 x가 뜻하는게 뭔가요?
# 제가 시리얼번호를 문자열로 받은 것 같은데요,
# 문자열(시리얼번호) 슬라이싱을 해서 분리한 다음에 요소 하나하나가 숫자인지 확인해 볼 필요 없이, 
# x를 반복시키면 왜 자동으로 문자열의 요소들이 하나하나 분리되는지 궁금합니다.




