# 백준 13975
# 파일 합치기 3

import sys

input = sys.stdin.readline

t = int(input())
sum = 0

for i in range(t):
    k = int(input())
    file_list = list(map(int, input().split()))
    file_list.sort()
    for i in range(k-1):
        temp = file_list[0]+file_list[1]
        file_list.append(temp)
        sum += temp
        file_list.pop(0)
        file_list.pop(1)
        file_list.sort()
    print(sum)
    file_list.clear()   
    


