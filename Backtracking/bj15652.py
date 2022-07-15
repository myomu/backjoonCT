# N과 M (4)

def backtracking(start):
    if len(numbers) == M:
        print(*numbers)
    else:
        for num in range(start, N+1): # 조건절은 없고 시작을 넘겨주어 자기와 같은 수 부터 시작하게끔 만들었다.
            numbers.append(num)
            backtracking(num)
            numbers.pop()

N, M = map(int, input().split())
numbers = []
backtracking(1)