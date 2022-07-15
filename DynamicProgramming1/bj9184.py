# 신나는 함수 실행

def w(a, b, c):
    if (a, b, c) in d:
        return d.get((a, b, c))
    else:
        if a <= 0 or b <= 0 or c<= 0:
            d[(a, b, c)] = 1
            return 1
        elif a > 20 or b > 20 or c > 20:
            d[(a, b, c)] = w(20, 20, 20)
            return w(20, 20, 20)
        elif a < b and b < c:
            d[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) # 다른 사람 풀이에는 이게 없던데..왜?
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            d[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

d = {}

while True:
    A, B, C = map(int, input().split())
    if A == -1 and B == -1 and C == -1:
        break
    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')



## 다른 사람 풀이1
## 내 코드보다 10배는 빠르고 코드수는 200B 더 적다.
import sys
read = sys.stdin.readline

cache = {}

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
        
    key = '{} {} {}'.format(a, b, c)
    
    ### 핵심코드 ###
    if key in cache:
        return cache[key]
    res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    cache[key] = res
    ################
    
    return res

while True:
    a,b,c = map(int, read().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))