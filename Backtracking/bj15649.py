# N과 M (1) // 순열 Permutation 또는 조합 Combination ??

from itertools import permutations

N, M = map(int, input().split())
item = [i for i in range(1, N+1)]
combi = list(permutations(item, M))

for j in combi:
    # for k in j:
    #     print(k, end=' ')
    # print()
    print(*j)

# 다른 사람 풀이 // permutations를 사용 안하고 구현.

def back_tracking():
    
    # stack의 길이가 M이 되면 출력
    if len(stack) == M:
        print(' '. join(list(map(str, stack))))
    else:
        for num in range(1, N+1):
            # num이 stack에 없으면
            if num not in stack:
                # stack에 추가하고 재귀
                stack.append(num)
                back_tracking()
                # 재귀함수 반환되면 pop
                stack.pop()
                
N, M = map(int, input().split())
stack = []
back_tracking()