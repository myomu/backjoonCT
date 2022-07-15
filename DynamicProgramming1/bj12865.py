# 평범한 배낭
# 잘 이해 안감..

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
bag = [[0, 0]]
bags = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    bag.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    w, v = bag[i][0], bag[i][1]
    for j in range(1, k+1):       
        if j < w:
            bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = max(bags[i-1][j], bags[i-1][j-w] + v)
        
print(bags[-1][-1])