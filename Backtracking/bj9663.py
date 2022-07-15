# N-Queen . 다른사람 문제 풀이 참고했음. -> 다른 방식 시도해볼것.

# def check(x):
#     # 범위가 N이 아니라 x 인 이유는 내가 놓을 퀸의 자리가 겹치는 경우가 생긴다.
#     # 무조건 리턴이 False가 되기 때문에 값(count)은 항상 0 이 된다.
#     for i in range(x): 
#         if board[x] == board[i] or abs(x-i) == abs(board[x]-board[i]):
#             return False
#     return True

def findQueen(x):

    global count
    if x == N:
        count += 1
        return
    
    for y in range(N):
        if not (column[y] or slash[x+y] or back_slash[x-y+N-1]):
            column[y] = slash[x+y] = back_slash[x-y+N-1] = 1
            findQueen(x+1)
            column[y] = slash[x+y] = back_slash[x-y+N-1] = 0

    # for y in range(N):
    #     board[x] = y
    #     if check(x):
    #         findQueen(x+1)
    # 위의 check() 함수를 사용하지 않는 방법으로 전환.. pypy로 돌려도 시간초과가 나옴.
    # 재귀마다 for문을 반복해서 그런가?


#board = [0]*N
N = int(input())
count = 0
column, slash, back_slash = [0]*N, [0]*(2*N-1), [0]*(2*N-1)
findQueen(0)
print(count)

