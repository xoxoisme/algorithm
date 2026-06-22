def solution(arr):
    return [arr[n] for n in range(len(arr)) if arr[n] != arr[n-1] or n == 0]