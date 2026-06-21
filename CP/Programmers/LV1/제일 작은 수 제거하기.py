def solution(arr):
    if arr[0] != 10: 
        arr.remove(min(arr))
        return arr
    else: return [-1]