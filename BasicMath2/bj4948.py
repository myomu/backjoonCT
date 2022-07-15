# 베르트랑 공준

def isPrime(min, max):
    max += 1 
    prime = [True] * max

    for i in range(2, int(max**0.5)+1):
        if prime[i]:
            for j in range(i*2, max, i):
                prime[j] = False

    numberOfDecimals = prime[min:].count(True)
    return numberOfDecimals

while True:
    n = int(input())

    if n == 0:
        break

    minR = n+1
    maxR = 2*n
    print(isPrime(minR, maxR))