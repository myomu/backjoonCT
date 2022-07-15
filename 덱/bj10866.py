# 덱

from collections import deque
import sys

N = int(input())
deq = deque()
bucket = []
for _ in range(N):
    command = sys.stdin.readline().split()
    cm = command[0]
    if cm == 'push_front':
        deq.appendleft(int(command[1]))
    elif cm == 'push_back':
        deq.append(int(command[1]))
    elif cm == 'pop_front':
        bucket.append(deq.popleft()) if len(deq) != 0 else bucket.append(-1)
    elif cm == 'pop_back':
        bucket.append(deq.pop()) if len(deq) != 0 else bucket.append(-1)
    elif cm == 'size':
        bucket.append(len(deq))
    elif cm == 'empty':
        bucket.append(1) if len(deq) == 0 else bucket.append(0)
    elif cm == 'front':
        bucket.append(deq[0]) if len(deq) != 0 else bucket.append(-1)
    elif cm == 'back':
        bucket.append(deq[-1]) if len(deq) != 0 else bucket.append(-1)

print(*bucket, sep='\n')