# 피보나치 수 5

def fibonacci(n):
    value = 0
    if n == 1:
        value = 1
    elif n > 0:
        value = fibonacci(n-1) + fibonacci(n-2) # fi(3) = fi(2) = (fi(1) + fi(0)) + fi(1) 총 fi는 5번 수행.
    # print(f"{n}", value)
    return value

n = int(input())
print(fibonacci(n))