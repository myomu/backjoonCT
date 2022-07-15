# 소인수분해
import math

## 방법1
n = int(input())

while n != 1:
    for i in range(2, n+1):
        
        if n%i == 0:
            print(i)
            n = n // i
            break
        else:
            continue

## 방법2
n = int(input())
d = 2
while n != 1:
    if n % d ==0:
        print(d)
        n /= d
    else:
        d += 1

## 방법3
def findFactor(n):
    print("넘겨받은 n", n)
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return i
        else:
            continue
    return n


n = int(input())

while n != 1:
    factor = findFactor(n)
    print(factor)
    n //= factor
