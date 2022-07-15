# 스택

import sys

stackLi = []

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    com = command[0]
    if com == 'push':
        stackLi.append(str(command[1]))
    elif com == 'pop':
        if len(stackLi) == 0:
            print(-1)
        else:
            print(stackLi[-1])
            del stackLi[-1]                
    elif com == 'size':
        print(len(stackLi))
    elif com == 'empty':
        if len(stackLi) == 0:
            print(1)
        else:
            print(0)
    elif com == 'top':
        if len(stackLi) == 0:
            print(-1)
        else:
            print(stackLi[-1])
