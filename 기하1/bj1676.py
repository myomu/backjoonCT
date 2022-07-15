# 팩토리얼 0의 개수
# bj2004번 문제와 동일한 방식. 참고할 것.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

N = int(input())
value = str(factorial(N))
cnt = 0
for i in reversed(range(len(value))):
    if value[i] == '0':
        cnt += 1
    else:
        break
print(cnt)


# 다른 사람 풀이.. 어떻게 푼지 잘 이해 안감.
def calc(n,v):
    ans=0
    i=v
    while i<=n:
        ans+=n//i
        i*=v
    return ans
n=int(input())
ans=calc(n,5)
print(ans)


# n과 m이 주어졌을 때 조합 nCm값의 끝에 0이 몇자리가 있는지 구하는 문제입니다.
# 직관적으로 봤을 때 n!과 m! n-m! 세가지를 직접구한후 0의 개수를 구하면 될 것 같지만
# n,m의 범위가 20억이기 때문에 20억! 의 값은 상상도 할 수 없을만큼 큰 수이기 때문에
# long long 자료형을 쓴다고 하더라도 저장할 수 없습니다.
# 때문에 20억!의 값을 구하지 않고도 0의 개수를 구할 수 있어야합니다. 

# 그렇다면 0의 개수는 어떻게 구할 수 있을까요?
# 끝자리에 0이 5개있는 수는 또 다른 수식으로 n * 10^5 로 표현할 수 있습니다.
# 이 수를 소인수 분해하면 5와 2의 짝이 5개 있다는것입니다.

# nCm의 값은 n!/m!*(n-m)! 이므로 각 n!, m! (n-m)!의 2와 5의 개수를 구한뒤에
# n!의 2의개수에 m!과 (n-m)!의 2의 개수를 합한값을 빼줍니다.
# 2의 개수를 빼주는것은 수식에서 약분을 하는것과 동일한 의미를 나타내기 때문입니다.
# 마찬가지로 5의 개수도 같은 식으로 구하여 nCm의 2의개수와 5의개수를 구한뒤
# min(2, 5)를 사용하면 2와5의 짝을 구할 수 있습니다.
