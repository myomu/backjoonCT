# 랜선 자르기
# 처음 first 를 0부터 시작하여 틀림..분모 나눌때 0으로 나누게되면 에러!
# 다음으로 틀린 점은 조건을 만족하는 것 중에서 최대의 길이를 가져야함으로..

import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

#print(lan)

first, last = 1, max(lan)
while first <= last:    
    mid = (first + last) // 2
    cnt = 0
    print(f'mid={mid}, cnt={cnt}, first={first}, last={last}')
    for i in lan:
        cnt += i // mid
    if cnt >= N:
        first = mid + 1
    elif cnt < N:
        last = mid - 1
    
print(last)