# 배수와 약수

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a == 0 or b == 0:
        continue
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')