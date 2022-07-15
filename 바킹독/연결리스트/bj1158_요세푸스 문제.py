# 요세푸스 문제

from collections import deque

N, K = map(int, input().split())
li = deque([i for i in range(1, N+1)])
s = []
while len(li) > 0:
    li.rotate(-(K-1))
    s.append(li.popleft())

print('<' + ', '.join(list(map(str, s))) + '>')

