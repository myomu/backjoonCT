# 최소공배수
import sys

def findLCM(a, b):
    number = []
    step = 1
    while True:
        if step > a or step > b:
            break
        if a%step == 0 and b%step == 0 and step != 1:
            a //= step
            b //= step
            number.append(step)
        else:
            step += 1   
    result = 1
    for i in number:
        result *= i 
    return result*a*b

t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(findLCM(a, b))



# 다른 사람 풀이. 간단한 코드. 그리고 빠르다. 위 방식의 1/40 정도?

num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a   
        # print(a,b)
    gcd = b
    lcm = A * B //b
    print(lcm)
