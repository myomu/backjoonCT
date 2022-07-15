# 키로거

import sys
from collections import deque

input = sys.stdin.readline
L = int(input())

for _ in range(L):
    left = []
    right = deque([])
    string = input().rstrip()
    for i in string:
        if i == '<':
            if left: right.appendleft(left.pop())
        elif i == '>':
            if right: left.append(right.popleft())
        elif i == '-':
            if left: left.pop()
        else:
            left.append(i)     
    print(''.join(left+list(right)))

