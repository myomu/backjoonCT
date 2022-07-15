# 숫자 카드2
# 딕셔너리로 풀었음. 딕셔너리 get 함수를 사용해 해당 key값이 없으면 0을 출력.

import sys

dic = dict()
N = int(input())
bucket = list(map(int, sys.stdin.readline().split()))
M = int(input())
mBucket = list(map(int, sys.stdin.readline().split()))

for i in bucket:
    dic[i] = 0
for i in bucket:
    dic[i] += 1
for j in mBucket:
    result = dic.get(j, 0)
    print(result, end = ' ')