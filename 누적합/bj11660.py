# 구간 합 구하기 5

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[0]*(N+1)]
sumOfM = [[0 for _ in range(N+1)] for _ in range(N+1)]
sumOfMRow = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
    matrix.append([0]+list(map(int, input().split())))

#sumOfM[1] = matrix[1]
for i in range(1, N+1):
    for j in range(1, N+1):
        sumOfM[j][i] = sumOfM[j-1][i] + matrix[j][i]

for i in range(1, N+1):
    for j in range(1, N+1):
        sumOfMRow[i][j] = sumOfM[i][j] + sumOfMRow[i][j-1]
# print(*matrix, sep='\n')
# print('------')
# print(*sumOfM, sep='\n')
# print('------')
# print(*sumOfMRow, sep='\n')

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (sumOfMRow[x2][y2]-sumOfMRow[x2][y1-1]) - (sumOfMRow[x1-1][y2]-sumOfMRow[x1-1][y1-1])
    print(result)