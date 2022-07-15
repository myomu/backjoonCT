# 단어 정렬
import sys

n = int(input())
bucket = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    bucket.append((word, len(word)))
setBucket = set(bucket)
sortBucket = sorted(setBucket, key=lambda x: (x[1], x[0]))

for i in sortBucket:
    print(i[0])