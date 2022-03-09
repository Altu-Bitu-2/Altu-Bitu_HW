# 백준 10804
# 카드 역배치

middle_arr = []
arr = list(range(1, 21))

for i in range(1, 11):
    a, b = map(int, input().split())
    middle_arr = arr[a-1:b] #해당 구간 잘라냄
    #print(middle_arr)
    middle_arr.reverse() #역배치 시킴
  
    arr[a-1:b] = middle_arr # 해당 부분에 대입
    
    for i in range(len(arr)):
        print(arr[i], end=' ')

# 백준 문제에서 주어진 예시 입력값과 출력값은 모두 동일하게 나오는데
# 어디서 틀렸는지 모르겠습니다..



    
    
