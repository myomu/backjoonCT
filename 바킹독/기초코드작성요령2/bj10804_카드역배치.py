# 카드 역배치

cards = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    bucket = cards[a-1:b]
    bucket.reverse() 
    cards[a-1:b] = bucket
    
print(*cards)

