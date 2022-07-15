# 피보나치 함수 // 날로 먹으려고 했다가 바로 시간초과 빠꾸먹음.. 메모제이션 이라는 기법을 사용
# 메모제이션은 매번 해당 값을 재귀로 구하지 않고 해당 값을 한 번 계산했으면 이를 저장해서 곧바로 불러오는 기법이다.
# 여러번 재귀할 필요 X.
import sys

fibo = {0:[1, 0], 1:[0, 1]}

def fibonacci(n):
    if n in fibo:
        return fibo[n]
    else:
        fibo[n] = [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]]
        return fibo[n]

t = int(input())
li = []
for i in range(t):
    li.append(int(sys.stdin.readline()))

for j in li:
    print(fibonacci(j)[0], fibonacci(j)[1])