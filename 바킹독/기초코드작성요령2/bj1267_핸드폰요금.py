# 핸드폰 요금

N = int(input())
bill = list(map(int, input().split()))

def findBill(b, rate, fee):
    return (b//rate+1)*fee

y, m = 0, 0
for i in bill:
    y += findBill(i, 30, 10)
    m += findBill(i, 60, 15)

if y == m:
    print('Y M', y)
else:
    if y > m:
        print('M', m)
    else:
        print('Y', y)
