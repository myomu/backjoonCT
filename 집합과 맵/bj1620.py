# 나는야 포켓몬 마스터 이다솜
# 숫자 판별하는 방법을 몰라서 get으로 못찾는 경우 else로 넘어가 number 딕셔너리에서 찾도록 하였다.
# isdigit을 사용하면 해당 문자가 숫자로 이루어져있는지 판단 가능하다.

import sys

N, M = map(int, input().split())
name = dict()

for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    name[pokemon] = str(i)

#딕셔너리 키-값을 반대로 만들어줌. 위의 for문에 딕셔너리 반대로하여 생성해도 되지만 이런 방식이 있다는 것을 확인하기 위해 사용.
number = dict(map(reversed, name.items())) 
li = []

for k in range(M):
    ans = sys.stdin.readline().strip()
    li.append(ans)

for answer in li:
    if name.get(answer, 0):
        print(name.get(answer))
    else:
        print(number.get(answer))
