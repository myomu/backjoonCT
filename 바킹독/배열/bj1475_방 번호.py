# 방 번호
# 반례 669

import math

N = input()
cards = [0 for _ in range(10)]
for i in N:
    num = int(i)
    cards[num] += 1

cards[6] = cards[9] = math.ceil((cards[6]+cards[9])/2)
#print(cards)
print(max(cards))