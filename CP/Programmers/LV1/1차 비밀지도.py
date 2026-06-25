def solution(n, arr1, arr2):
    or_res = [bin(i|j)[2:].zfill(n) for i, j in zip(arr1, arr2)]
    return [s.replace('0', ' ').replace('1', '#') for s in or_res]