# 알고리즘 수업 - 피보나치 수 1
# 처음 조건 1을 그대로 count 했을 때 시간초과가 나온다. 원론적인 법칙을 찾아보니..
# cntFib 는 그냥 피보나치 수열의 더하는 값을 그냥 구하면 된다. fib(5) = 5가 나오는데 이게 조건1의 count 값과 동일한셈이다.
# cntFibonacci는 입력된 N-2 의 값을 가진다.

# def fib(n):
#     global cntFib
#     if n == 1 or n == 2:
#         cntFib += 1 # 조건 1
#         return 1
#     else:
#         return (fib(n-1) + fib(n-2))

def fibonacci(n):
    # global cntFibonacci
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        # cntFibonacci += 1 # 조건2
    return f[n]

N = int(input())
# cntFibonacci = 0
f = [1 for _ in range(N+1)]

print(fibonacci(N), N-2)