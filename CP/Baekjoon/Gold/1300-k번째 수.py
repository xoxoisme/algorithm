N = int(input())
K = int(input())
start = 1
end = K

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, N+1):
        count += min(mid // i, N)
    if count >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(result)