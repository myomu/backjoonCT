# AC 

from collections import deque

deq = deque()
T = int(input())
for _ in range(T):
    command = input()
    n = int(input())
    # 처음에 원소가 없더라도 error가 아닐 수 있습니다.
    # try:
    #     li = deque(list(map(int, input()[1:-1].split(','))))
    # except:
    #     print('error')
    #     continue
    try :
        li = deque(list(map(int, input()[1:-1].split(','))))
    except:
        li = []
    direction = True
    errorCheck = True

    for i in command:
        if i == 'R':
            if direction == True:
                direction = False
            else:
                direction = True
        elif i == 'D':
            if direction == True:
                try:
                    li.popleft()
                except:
                    print('error')
                    errorCheck = False
                    break
            elif direction == False:
                try:
                    li.pop()
                except:
                    print('error')
                    errorCheck = False
                    break
    
    if direction == True and errorCheck == True:
        print("[" + ",".join(list(map(str, li))) + "]")
    elif direction == False and errorCheck == True:
        print("[" + ",".join(list(map(str, reversed(li)))) + "]")