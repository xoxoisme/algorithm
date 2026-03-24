N = int(input())

arr = list(map(int, input().split()))

# 그냥 정렬하지 말고, 1개, 2개, 3개가 나오는 경우의 최소값을 따라 구하자
min_lists = []
if N == 1:
    arr.sort()
    res = sum(arr[:5])
else:
    min_lists.append(min(arr[0], arr[5]))
    min_lists.append(min(arr[1], arr[4]))
    min_lists.append(min(arr[2], arr[3]))
    min_lists.sort()

    one_n = (N - 2) * (5 * N - 6)
    two_n = 4 * (2 * N - 3)
    three_n = 4

    res = min_lists[0] * one_n
    res += min_lists[0] * two_n + min_lists[1] * two_n
    res += sum(min_lists) * 4

print(res)