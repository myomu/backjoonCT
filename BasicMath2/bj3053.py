# 택시 기하학
# 유클리드 기하학의 원의 넓이는 pi*r(반지름)^2
# 택시 기하학의 원의 넓이는 (마름모이므로) r^2 * 2 이다.

import math

r = int(input())

print(round(r*r*math.pi, 6))
print("%0.6f" %(r*r*2)) # 파이썬은 콤마(,)가 아닌 %를 쓴다.
