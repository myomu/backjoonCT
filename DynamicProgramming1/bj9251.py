# LCS

import sys

input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
row, col = len(s1), len(s2)
matrix = [[0]*(col+1) for _ in range(row+1)] # 이 부분 행 열을 반대로 설정해 런타임 에러 발생함..

for i in range(1, row+1):
    for j in range(1, col+1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

print(matrix[row][col])

## 다른 사람 풀이
# 훨씬 빠르더라
string1, string2 = input().strip(), input().strip()

dp = [0] * len(string2)

for i in range(len(string1)):
    cnt = 0
    for j in range(len(string2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif string1[i] == string2[j]:
            dp[j] = cnt + 1
            
print(max(dp))