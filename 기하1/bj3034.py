# 앵그리 창영
import sys

n, w, h = map(int, input().split())
ans = []

for i in range(n):
    length = int(sys.stdin.readline().strip())
    if length <= (w**2 + h**2)**(0.5):
        ans.append('DA')
    else:
        ans.append('NE')

print(*ans, sep='\n')