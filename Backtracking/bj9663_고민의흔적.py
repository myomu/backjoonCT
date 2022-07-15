# N-Queen

def check(N, x, y):
    # x와 y 위치의 칸을 전부 1로.
    for i in range(N):
        board[x][i] = 1
        board[i][y] = 1
    # 대각선 위치의 칸을 전부 1로.
    x1 = x2 = x3 = x4 = x
    y1 = y2 = y3 = y4 = y
    while True:
        btn1 = btn2 = btn3 = btn4 = 0
        if x1 < N and y1 > -1:
            board[x1][y1] = 1
            x1 += 1
            y1 -= 1
        else:
            btn1 = 1
        if x2 > -1 and y2 > -1:
            board[x2][y2] = 1
            x2 -= 1
            y2 -= 1
        else:
            btn2 = 1
        if x3 > -1 and y3 < N:
            board[x3][y3] = 1
            x3 -= 1
            y3 += 1         
        else:
            btn3 = 1
        if x4 < N and y4 < N:
            board[x4][y4] = 1
            print(x4, y4)
            x4 += 1
            y4 += 1    
        else:
            btn4 = 1
        if (btn1, btn2, btn3, btn4) == (1, 1, 1, 1):
            break

def findQueen(N):
    print(board)
    # if len(board) == N:
    #     count += 1
    #     return
    global count
    if count == 8:
        sum += 1
        #print(sum)
        return
    else:
        for x in range(N):
            for y in range(N):
                #if board[-1][0] != x and board[-1][1] != y:
                if not board[x][y]: # board의 칸이 0이면 실행. 1이면 둘 수 없는 곳.
                    count += 1
                    print(count, (x, y))
                    check(N, x, y)
                    #board.append((x, y))       
                    findQueen(N)
                    count -= 1
                    #board.pop()
    
count = 0
sum = 0
N = int(input())
board = [[0]*N]*N # N*N 칸을 만들고 각 칸을 0으로 채운다.
findQueen(N)
print(sum)