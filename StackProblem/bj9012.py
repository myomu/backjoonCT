# 괄호
import sys

T = int(input())
for i in range(T):
    PS = sys.stdin.readline().rstrip()
    if len(PS)%2 != 0 or PS[0] == ')' or PS[-1] == '(':
        print('NO')
    else:
        count = 0
        for j in PS:
            if j == '(':
                count += 1
            if j == ')':
                count -= 1
            if count < 0:
                break
        if count == 0:
            print('YES')
        else:
            print('NO')
