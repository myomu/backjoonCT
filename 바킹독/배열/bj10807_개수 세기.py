# 개수 세기
# 처음에 음수 부분을 생각하지 않아서 바로 틀림..
# 짧은 코드들을 보면 count 함수를 통해 그냥 findNum을 찾는다. li.count(findNum)
# defaultdict 를 이용하는 방법도 있다. 디폴트 딕셔너리(유사 딕셔너리)는 키의 값이 정해지지 않으면 값을 0으로 초기화한다.

'''
N = int(input())
numbers = list(map(int, input().split()))
findNum = int(input())
plusLi = [0 for _ in range(101)]
minusLi = [0 for _ in range(101)]

for num in numbers:
    if num >= 0:
        plusLi[num] += 1
    else:
        minusLi[-num] += 1
if findNum >= 0:
    print(plusLi[findNum])
else:
    print(minusLi[-findNum])
'''


