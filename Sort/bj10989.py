# 수 정렬하기 3. 카운팅 소트라는 정렬 방법으로 구현.
# 이 방식은 N의 값이 크면 시간 복잡도가O(n) 이 아닌 O(n+K)가 된다고 한다.

## 1. 아래 방식은 단순 횟수만 저장해서 출력하는 방식.
import sys

MAX_NUM = 10001

N = int(sys.stdin.readline())

basket = [0]*MAX_NUM

for _ in range(N):
    n = int(sys.stdin.readline())
    basket[n] += 1

# for i in range(1, len(basket)):
#     basket[i] += basket[i-1]

for j in range(len(basket)):
    if basket[j] != 0:
        for k in range(basket[j]):
            sys.stdout.write(str(j) + '\n')

## 2. 카운팅 소트 방식
import sys

MAX_NUM = 10001

N = int(sys.stdin.readline())

basket = [0]*MAX_NUM
number = []

for _ in range(N):
    n = int(sys.stdin.readline())
    basket[n] += 1
    number.append(n)

for i in range(1, len(basket)):
    basket[i] += basket[i-1]

for j in range(len(basket)):
    if basket[j] != 0:
        for k in range(basket[j]):
            sys.stdout.write(str(j) + '\n')

