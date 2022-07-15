# 큐

from collections import deque
import sys

deq = deque()
bucket = []

N = int(input())
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        deq.append(int(command[1]))
    elif command[0] == 'pop':
        if len(deq) == 0:
            bucket.append(-1)
        else:
            bucket.append(deq.popleft())
    elif command[0] == 'size':
        bucket.append(len(deq))
    elif command[0] == 'empty':
        if len(deq) == 0:
            bucket.append(1)
        else:
            bucket.append(0)
    elif command[0] == 'front':
        if len(deq) == 0:
            bucket.append(-1)
        else:
            bucket.append(deq[0])
    elif command[0] == 'back':
        if len(deq) == 0:
            bucket.append(-1)
        else:
            bucket.append(deq[-1])

print(*bucket, sep='\n')