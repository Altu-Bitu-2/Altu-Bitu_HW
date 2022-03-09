# 백준 1026
# 보물

import sys

input = sys.stdin.readline

number = int(input()) # n 입력

list_a = list(map(int, input().split())) # 정수 배열 a 입력
list_b = list(map(int, input().split())) # 정수 배열 b 입력

multiply_ab = [] #a배열 숫자와 b배열 숫자를 곱셈한 숫자들을 모아 놓은 배열

list_a.sort() # a 오름차순으로 정렬
for i in range(number):
    x = max(list_b) # 배열 b에서 가장 큰 수를 꺼냄
    multiply_ab.append(list_a[i]*x) 
    # 정렬된 리스트 a에서 첫 번째 숫자와 배열 b에서 가장 큰 수를 곱함
    list_b.remove(x) # 해당 숫자 이미 곱했으므로 삭제

sum = 0

for i in range(len(multiply_ab)):
    sum += multiply_ab[i] # 곱했던 숫자들을 모두 더함

print(sum)

# a 정렬하기
# b -> max함수 이용해서 가장 큰 값만 가져오기 (pop 해서 삭제시키고..)
# 정렬된 a에서 차례로 숫자를 꺼내서 max(list_b)와 곱하기
# 곱해놓은 숫자들을 한꺼번에 더해서 결과 도출

