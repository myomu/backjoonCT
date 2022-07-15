# 최대공약수와 최소공배수

a, b = map(int, input().split())

step = 1
bucket = []
maxValue = max(a, b)
while True:
    if step > maxValue:
        break
    if a%step == 0 and b%step == 0 and step != 1:
        a //= step
        b //= step
        bucket.append(step)
    else:
        step += 1
#print(bucket, a, b)
lcm = gcf = 1
for i in bucket:
    gcf *= i
lcm = gcf*a*b

print(gcf, lcm)