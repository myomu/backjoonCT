# 연산자 끼워넣기

from itertools import permutations
import sys

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
bucket = []

for i in range(4):
    if i == 0:
        bucket += '+' * operator[i]
    elif i == 1:
        bucket += '-' * operator[i]
    elif i == 2:
        bucket += '*' * operator[i]
    elif i == 3:
        bucket += '/' * operator[i]
    else:
        print('err')

nextBucket = list(permutations(bucket, N-1))
nextBucket = list(set(nextBucket)) # 여기서 set 함수를 통해 중복된 것을 제거해줌. 안했을 때 시간초과 나왔음.
result = []

for p in nextBucket:
    sum = number[0]
    for j in range(1, N):
        if p[j-1] == '+':
            sum += number[j]
        elif p[j-1] == '-':
            sum -= number[j]
        elif p[j-1] == '*':
            sum *= number[j]
        elif p[j-1] == '/':
            if sum < 0:
                sum = -sum
                sum //= number[j]
                sum = -sum
            else:
                sum //= number[j]
    result.append(sum)

print(max(result))
print(min(result))


## 다른 사람 풀이. permutation 모듈 사용없이 풀었더라. 함수를 재귀방식으로 사용해서 전체를 탐색하는 방식을 사용함.
## 모든 if 문을 순환하게 하여 각 조건을 찾도록 했더라.

from sys import stdin

input = stdin.readline

N = int(input())  # 정점의 개수
nodes = list(map(int, input().split()))  # 노드 리스트
ops = list(map(int, input().split()))  # 연산자 리스트

maximum = -10e9
minimum = 10e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum
    global minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 각각 if를 준다는 것에 주목!!!!!
    # 각각 if를 줌으로써 dfs내의 매개변수들의 값이 조건을 통과하면 매개변수의 변화없이 모든 조건에 다 들어갈 수 있게 한다.
    if plus:
        dfs(depth + 1, total + nodes[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nodes[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nodes[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1,
            (total //
             nodes[depth]) if total >= 0 else -(-total // nodes[depth]), plus,
            minus, multiply, divide - 1)


dfs(1, nodes[0], ops[0], ops[1], ops[2], ops[3])
print(maximum)
print(minimum)