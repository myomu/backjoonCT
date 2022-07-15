# 듣보잡
import sys

N, M = map(int, input().split())
dic = dict()
bucket = []

for i in range(N):
    hearing = sys.stdin.readline().strip()
    dic[hearing] = 1

for j in range(M):
    seeing = sys.stdin.readline().strip()
    if dic.get(seeing, 0):
        bucket.append(seeing)

bucket.sort()
print(len(bucket))
print(*bucket, sep='\n')