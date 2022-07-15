# 별 찍기 - 7

N = int(input())
count = 2*N - 1
for i in range(1, count+1):
    if i <= N:
        print(' '*(N-i) + '*'*(2*i - 1))
    else:
        print(' '*(i-N) + '*'*(count - 2*(i-N)))

'''
훨씬 깔끔함..

for i in range(1, n):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
'''