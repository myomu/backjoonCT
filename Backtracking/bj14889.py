# 스타트와 링크
import sys
from itertools import combinations

N = int(input())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
number = [x for x in range(N)]#[[x, y] for x in range(N) for y in range(N) if x != y]
team = list(combinations(number, N//2))

def cal(arr):
    #print('arr=', arr)
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            row = arr[i]
            col = arr[j]
            sum += table[row][col] + table[col][row]
            #print(f'i={row}, j={col}, sum={sum}')
    #print(sum)
    return sum

min = 100000
for i in range(len(team)//2):
    diff = abs(cal(team[i]) - cal(team[len(team)-i-1]))
    if diff < min:
        #print(diff)
        min = diff

print(min)
