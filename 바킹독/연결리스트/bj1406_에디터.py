# 에디터
# 스택을 두 개로 나누어 생각한다. 두 개의 스택 사이를 커서라고 가정하는 방식임.

from collections import deque
import sys

input = sys.stdin.readline
string = input().rstrip() # rstrip() 안해주면 틀렸다고 나왔었음..!
M = int(input())

left = list(string)
right = deque([])

for _ in range(M):
    command = input().split()
    print(command)
    if command[0] == 'P':
        left.append(command[1])
    elif command[0] == 'B':
        if left: left.pop()
    elif command[0] == 'L':
        if left: right.appendleft(left.pop())
    elif command[0] == 'D':
        if right: left.append(right.popleft())
    #print(left, right)

result = ''.join(left+list(right))
print(result)