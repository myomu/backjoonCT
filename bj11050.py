# 이항 계수1

N, K = map(int, input().split())
result = 0

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

result = int(factorial(N) / (factorial(K)*factorial(N-K)))
print(result)