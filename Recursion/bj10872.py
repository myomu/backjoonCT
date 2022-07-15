# 팩토리얼

# n = int(input())

# t = 1
# for i in range(1, n+1):
#     t *= i

# print(t)

# 팩토리얼 문제니까..

n = int(input())

def factorial(n):
    result = 1
    if n > 0:
        result = n*factorial(n-1)
    return result

print(factorial(n))
