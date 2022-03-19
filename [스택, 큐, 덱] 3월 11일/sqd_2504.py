# 백준 2504
# 괄호의 값

import sys

input = sys.stdin.readline

bracket = input().rstrip() # 괄호 입력
stack=[]

bracket_pair=dict()
bracket_pair[')']='('
bracket_pair[']']='['

bracket_value=dict()
bracket_value['('] = 2
bracket_value['['] = 3





# 질문) 튜터링 시간 때 풀었던 문제와 비슷한 결인 것은 알겠는데 어떻게 풀어야 할지 감이 잘 안 잡혀요ㅠㅠ
#       스택의 top(열린 괄호)과 비교할 때 짝이 맞는 경우에 이게 []인지, [x]인지 판단을 어떻게 해야 하는지 잘 모르겠습니다.
#       