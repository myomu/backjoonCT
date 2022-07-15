# N과 M (2) 이번에는 순열permutation이 아닌 조합combination을 요구하고 있다.


def combi(start): # 매개변수로 앞서 재귀가 발생시 for문의 num을 넘겨서 이것보다 큰 수여야만 num을 추가할수 있게 하였다.
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
    else:
        for num in range(1, N+1):
            if num <= start:
                continue
            if num not in numbers:
                numbers.append(num)
                combi(num) # 예를들어 start가 1이고 num이 2여서 위 조건을 클리어하면 재귀를 통해 (1, 2)가 만족된다.
                numbers.pop() # start가 2이면 위 조건에 의해서 (2, 1) 이런 것은 넘어가게 된다. (2, 3) (2, 4) 이런 것만 만족된다.

N, M = map(int, input().split())
numbers = []
combi(0)


