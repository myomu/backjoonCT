# 대칭 차집합
# 리스트 합집합, 교집합, 차집합, 대칭 차집합. set을 이용..|, &, -, ^
import sys

A, B = map(int, input().split())
a_list = list(map(int, sys.stdin.readline().strip().split()))
b_list = list(map(int, sys.stdin.readline().strip().split()))

symmetric = list(set(a_list) ^ set(b_list))

print(len(symmetric))