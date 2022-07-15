# 참외밭
# 덱의 특성을 이용. rotate를 사용하여 한칸씩 리스트를 이동시킨다.
# 아이디어는 전체 사각형에서 작은 사각형을 빼는 방식이다.
# 그리고 한 변의 앞뒤는 높이 또는 너비이다. 만약 임의의 한 변이 너비이면 앞 뒤의 값은 높이인 셈이다.
# 먼저 큰 사각형의 너비와 높이를 구하고 작은 너비와 높이는 각각의 합이 큰 사각형의 너비와 높이가 되므로 이 합에 부합하는
# 조건을 찾는다.
# 이 합의 조건에 맞는 사이의 높이 혹은 너비야말로 작은 사각형의 너비와 높이가 된다.

from collections import deque

area = int(input())
w = []
h = []
li = []

for _ in range(6):
    direction, length = map(int, input().split())
    li.append(length)
    if direction in [1, 2]:
        w.append(length)
    elif direction in [3, 4]:
        h.append(length)

small_w = 0
small_h = 0
li = deque(li)

for i in range(6):
    if max(w) == li[0] + li[2]:
        small_h = li[1]
    if max(h) == li[0] + li[2]: # 이 부분을 elif 로 했을 때 틀림. 정사각형일 때 elif 면 틀린다..
        small_w = li[1]
    li.rotate(-1)

result = area * ((max(w)*max(h)) - (small_w*small_h))
print(result)


