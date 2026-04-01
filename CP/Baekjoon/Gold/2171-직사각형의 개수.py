import sys
input = sys.stdin.readline

n = int(input())

l = []
nums = set()
index = 0
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
    nums.add(x)
    nums.add(y)
nums = sorted(list(nums))
dnums = {}
for a in range(len(nums)):
    dnums[nums[a]] = a
 
dx = {}
dy = {}
for i in l:
    x = dnums[i[0]]
    y = dnums[i[1]]
    if x in dx:
        dx[x].append(y)
    else:
        dx[x] = [y]
    if y in dy:
        dy[y].append(x)
    else:
        dy[y] = [x]


count = 0
for i in dx:
    if len(dx[i]) >= 2:
        for j in range(len(dx[i]) - 1) :
            for j2 in range(j + 1,len(dx[i])):
                p1 = dx[i][j]  
                p2 = dx[i][j2] 
                    
                for k in dy[p1]:
                    if k > i:
                        if k in dy[p2]:
                            count += 1
print(count)   