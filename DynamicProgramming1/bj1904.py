# 01타일
# 규칙성이 있는 문제..
# 찾아보니 N-1의 뒤에 1을, N-2의 뒤에 00을 붙여주는 방식을 사용하더라.
# b[0] = 0
# b[1] = 1 # 1
# b[2] = 2 # 11, 00
# b[3] = 3 # 100, 111, 001
# b[4] = 5 # 1100, 0000, 1001, 1111, 0011
# 이런식이다.. 결국은 N-1 + N-2 의 값이 N의 개수의 값이 되는 셈.

N = int(input())

b = {}
b[1] = 1
b[2] = 2

for i in range(3, N+1):
    b[i] = (b[i-1] + b[i-2])%15746 # 여기서 계속 나눠주는 이유는 값이 계속 커지면 할당되는 메모리가 계속 커지기 때문에 그렇다.
                                    # 최종적으로 구하는 값에서 나누는 것이 아닌 수시로 나눠주는 것이 포인트.

print(b[N]%15746)
