# 문자열 집합
import sys

N, M = map(int, input().split())
dic = dict()
cnt = 0

for i in range(N+M):
    if i < N:
        st = sys.stdin.readline().strip()
        dic[st] = 1
    else:
        st2 = sys.stdin.readline().strip()
        if dic.get(st2, 0):
            cnt += 1

print(cnt)
