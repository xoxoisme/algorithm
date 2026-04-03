t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    distance = y - x
    tmp = 0 
    count = 0 
    moving = 0 

    while tmp < distance:
        count += 1
        if count % 2 != 0:
            moving += 1
        tmp += moving
    print(count)