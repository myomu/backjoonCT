# 제로

import sys

K = int(input())
bucket = []

for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0 and len(bucket) > 0:
        bucket.pop()
    else:
        bucket.append(num)

print(sum(bucket))