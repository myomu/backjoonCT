# 큐 2
# 이 부분은 deque 라는 것을 사용한다. pop(0)을 사용하면 리스트의 0번째 자리의 수를
# 리스트의 가장 끝자리로 옮기고 삭제하여 시간 복잡도가 높다. [0, 1, 2] -> [1, 0, 2] -> [1, 2, 0] -> [1, 2]
# deque를 사용하면 리스트 바로 앞의 숫자를 삭제함으로 속도가 빠르다.
import sys
from collections import deque

n = int(input())
bucket = deque()
for i in range(n):
    line = list(map(str, sys.stdin.readline().split()))
    if line[0] == 'push':
        bucket.append(int(line[1]))
    elif line[0] == 'front':
        if len(bucket) != 0:
            print(bucket[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if len(bucket) != 0:
            print(bucket[-1])
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(bucket))
    elif line[0] == 'empty':
        if len(bucket):
            print(0)
        else:
            print(1)
    elif line[0] == 'pop':
        if len(bucket) != 0:
            print(bucket.popleft())
        else:
            print(-1)
    else:
        print('err')