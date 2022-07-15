# 회전하는 큐

from collections import deque

N, M = map(int, input().split())
numbers = deque([i for i in range(1, N+1)])
findNum = list(map(int, input().split()))
cnt = 0

for i in range(M):
    num = findNum[i]  
    halfLen = len(numbers) / 2
    while True:
        if num == numbers[0]:
            numbers.popleft()
            break
        elif numbers.index(num) > halfLen:
            numbers.rotate(1)
            cnt += 1
        else:
            numbers.rotate(-1)
            cnt += 1
print(cnt)
