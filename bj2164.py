# 카드2
from collections import deque

n = int(input())
li = [i for i in range(1, n+1)]
li = deque(li)

while True:
    if len(li) == 1:
        break
    li.popleft()
    li.append(li.popleft())

print(li[0])