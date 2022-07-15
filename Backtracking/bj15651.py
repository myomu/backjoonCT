# N과 M (3) // 중복된 수도 함께 반복하므로 이전의 if 조건문을 빼고 그대로 넣음.

def tracking():
    if len(numbers) == M:
        print(*numbers)
    else:
        for num in range(1, N+1):
            numbers.append(num)
            tracking()
            numbers.pop()


N, M = map(int, input().split())
numbers = []
tracking()