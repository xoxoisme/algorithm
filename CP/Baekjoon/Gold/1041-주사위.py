N = int(input())

arr = list(map(int, input().split()))

# 그냥 정렬하지 말고, 1개, 2개, 3개가 나오는 경우의 최소값을 따라 구하자
arr.sort()

one = (N - 2) * (5 * N - 6)
two = 4 * (2 * N - 3)
three = 4

res = arr[0] * one
res += arr[0] * two + arr[1] * two
res += sum(arr[:3]) * 4

print(res)