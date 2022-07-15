# ATM

N = int(input())
times = list(map(int, input().split()))
sumTimes = [0 for _ in range(N)]
times.sort()
sumTimes[0] = times[0]

for i in range(1, N):
    sumTimes[i] = sumTimes[i-1] + times[i]

print(sum(sumTimes))