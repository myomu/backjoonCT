# 오큰수
# 해결 방법 못 찾아서 다른 사람 풀이 참고하였음.. 지금도 잘 이해는 안간다. https://hongcoding.tistory.com/40
# stack에 수열의 수가 아닌 위치를 저장함은 result에 해당 위치에 수를 담아 나중에 출력하고자 함.

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
result = [-1]*N
stack = []

for i in range(N):
    stack.append(i)
    if i == N-1:
        break
    while stack and A[stack[-1]] < A[i+1]:
        result[stack.pop()] = A[i+1]

print(*result)


# 아래가 참고한 소스코드 원본
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        
        answer[stack.pop()] = A[i]
        print(f'answer= {answer}')
    stack.append(i)
    print(f'i={i}, stack={stack}, answer={answer}')


print(*answer)