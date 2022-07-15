# # 스도쿠

# # 아이디어1.
# # 행, 열, 박스 안을 각 체크하고 0이 하나인 경우를 체크한다.
# # 0이 하나인 경우 나머지 숫자를 찾는다.
# # 아이디어2.
# # 1~9 의 합은 45이다. 나머지 숫자 = 45 - (나머지 수의 합)

# def printTable():
#     for i in table:
#         print(*i)

# def checkZero():
#     global count
#     for i in table:
#         for j in i:
#             if j == 0:
#                 count += 1

# def checkRow(row):
#     sum = checkZero = ROW = COLUMN = 0
#     for c in range(9):
#         if table[row][c] == 0:
#             checkZero += 1
#             ROW, COLUMN = row, c
#         if checkZero > 1:
#             return False
#         sum += table[row][c]
#     table[ROW][COLUMN] = 45-sum
#     global cnt
#     cnt += 1
#     return True

# def checkColumn(column):
#     sum = checkZero = ROW = COLUMN = 0
#     for r in range(9):
#         if table[r][column] == 0:
#             checkZero += 1
#             ROW, COLUMN = r, column
#         if checkZero > 1:
#             return False
#         sum += table[r][column]
#     table[ROW][COLUMN] = 45-sum
#     global cnt
#     cnt += 1
#     return True

# # 기준이 되는 start 지점을 찾는게 우선.
# # startRow = row - row%3, startColumn = column - column%3
# def checkBox(row, column): 
#     sum = checkZero = ROW = COLUMN = 0
#     startRow = row - row%3
#     startColumn = column - column%3
#     for i in range(3):
#         for j in range(3):
#             if table[startRow+i][startColumn+j] == 0:
#                 checkZero += 1
#                 ROW, COLUMN = startRow+i, startColumn+j
#             if checkZero > 1:
#                 return False
#             sum += table[startRow+i][startColumn+j]
#     table[ROW][COLUMN] = 45-sum
#     global cnt
#     cnt += 1
#     return True

# def sudoku():
#     global cnt
#     if cnt == count:
#         return
#     for row in range(9):
#         for column in range(9):
#             if table[row][column] == 0:
#                 cnt += 1
#                 # 동시에 함수를 실행시키면 안된다. 기준 좌표를 0,0으로 넘기면 먼저 checkRow가 0,0에 1을 할당하게되고
#                 # checkColumn이 그후 0,0을 기준으로 파악하여 남는 4자리 2,0 에 들어가야할 것을 0,0에 넣게된다.
#                 # 그러므로 0,0 의 출력이 4가 되는 것.
#                 # 오류 참고..RecursionError: maximum recursion depth exceeded while calling a Python object
#                 # 과도한 recursion에는 한계가 있다.
#                 if checkRow(row) or checkColumn(column) or checkBox(row, column): #or checkColumn(row, column) or checkBox(row, column):
#                     sudoku()
#                 else:
#                     continue

# table = []
# count = cnt = 0
# for _ in range(9):
#     line = list(map(int, input().split()))
#     table.append(line)

# checkZero()
# sudoku()
# printTable()




# 다른 사람 풀이. 이 풀이대로 해야만 모든 조건을 탐색할 수 있다. 백트래킹에 걸맞은 코드라고 볼 수 있다.
# 위의 내가 생각한 아이디어는 스도쿠에 0이 하나인 것만 파악하여 푸는 방식이다.
# 모든 칸이 0일 경우 어떻게 해야할지는 제시하지 못한다.
# import sys


# def is_possible(depth):
#     global chess
#     global pos
#     row = pos[depth][0]
#     col = pos[depth][1]
#     for i in range(9):
#         if chess[row][i] == chess[row][col] and i != col:
#             return 0
#         elif chess[i][col] == chess[row][col] and i != row:
#             return 0
#     for i in range((row // 3) * 3, (row // 3) * 3 + 3):
#         for j in range((col // 3) * 3, (col // 3) * 3 + 3):
#             if chess[i][j] == chess[row][col] and i != row and j != col:
#                 return 0
#     return 1


# def sudoku(depth):
#     if depth == count:
#         for i in chess:
#             print(' '.join(map(str, i)))
#         exit(0)
#     else:
#         for i in range(1, 10):
#             chess[pos[depth][0]][pos[depth][1]] = i
#             if is_possible(depth):
#                 sudoku(depth + 1)
#             chess[pos[depth][0]][pos[depth][1]] = 0


# chess = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# pos = [[x, y] for x in range(9) for y in range(9) if chess[x][y] == 0]
# count = len(pos)

# sudoku(0)


# exit(0)를 사용하지 않고 종료하면 시간초과가 나온다...ㅎㅎ;; 계속 return하여 종료시켜줘야 해서 그런가 보다.
# 그래도 시간초과 나와서 pypy3 로 통과햇다.. 허;;
import sys

def printTable():
    for i in table:
        print(*i)

def check(row, col):
    for i in range(9):
        if table[i][col] == table[row][col] and i != row:
            return 0
        if table[row][i] == table[row][col] and i != col:
            return 0
    startRow = row - row%3
    startCol = col - col%3
    for x in range(3):
        for y in range(3):
            if table[startRow+x][startCol+y] == table[row][col] and startRow+x != row and startCol+y != col:
                return 0
    return 1

def sudoku(line):
    global cnt
    if line == len(zeroPoint): # 0인 숫자를 한 칸 채우면 다음 sudoku에선 line +1 값을 넘겨 하나 체크되었음을 확인. 최종적으로 모든 0을 채우면 종료. exit(0)가 필요하다.
        cnt = 1
        #print()
        #printTable()
        return
        #exit(0)

    for i in range(1, 10):        
        #print(f'line={line}, i={i}')
        x, y = zeroPoint[line][0], zeroPoint[line][1]
        table[x][y] = i
        if check(x, y):
            sudoku(line+1)
        if cnt:
            break
        table[x][y] = 0

table = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeroPoint = [[x, y] for x in range(9) for y in range(9) if table[x][y] == 0]

cnt = 0
sudoku(0)
printTable()


# 아래 사람 풀이 참고할 것. 이 사람 풀이가 시간이 나의 것의 1/3 정도 된다..!
sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]

def find(i, j):
    visited = [0] * 10

    for k in range(9):
        visited[sudoku[i][k]] = 1
        visited[sudoku[k][j]] = 1

    r = i//3 * 3
    c = j//3 * 3

    for x in range(r, r + 3):
        for y in range(c, c + 3):
            visited[sudoku[x][y]] = 1
    
    temp = [i for i in range(1, 10) if not visited[i]]
    return temp

cp = False
def dfs(index):
    global cp
    if cp:
        return

    if index == len(zeros):
        for i in range(9):
            print(' '.join(list(map(str, sudoku[i]))))
        cp = True
        return
    else:
        i, j = zeros[index]
        for k in find(i, j):
            sudoku[i][j] = k
            dfs(index + 1)
            sudoku[i][j] = 0

dfs(0)
