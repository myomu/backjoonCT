# 체스판 다시 칠하기
# 다른 사람 블로그 보고 풂..ㅋㅋ;;
import sys

N, M = map(int, input().split()) # N은 (행), M은 (열)
board = []
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    board.append(line)

bucket = ['WBWBWBWB', 'BWBWBWBW']
result = []

for row in range(N-7): # N-7과 M-7은 행 열의 첫 시작점 위치를 제한 하는 것.
    for col in range(M-7): # 즉, [row][col] 이 가장 왼쪽 상단 시작 점을 말한다.
        firstW = 0
        firstB = 0
        for x in range(row, row+8):
            for y in range(col, col+8):
                if x%2 == 0: # 짝수 행
                    if board[x][y] != bucket[0][y%8]:
                        firstW += 1
                    if board[x][y] != bucket[1][y%8]:
                        firstB += 1

                else: # 홀수 행
                    if board[x][y] != bucket[1][y%8]:
                        firstW += 1
                    if board[x][y] != bucket[0][y%8]:
                        firstB += 1
        result.extend([firstW, firstB])

print(min(result))

        