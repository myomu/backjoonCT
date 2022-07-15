# 수 정렬하기 2 //nlogn의 시간 복잡도를 요구함. 일단은 내장함수 sort를 이용. 나중에 병합, 힙 정렬을 사용해보자.

import sys

n = int(sys.stdin.readline())
number = []
for _ in range(n):
    num = int(sys.stdin.readline())
    number.append(num)
number.sort()
for i in number:
    print(i)