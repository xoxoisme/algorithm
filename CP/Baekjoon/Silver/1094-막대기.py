X = int(input())

count = 0
n = 64
while X > 0:
    if n > X:
        n //= 2
    else:
        count += 1
        X -= n

print(count)