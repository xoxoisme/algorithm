def solution(ingredient):
    burger = [1, 2, 3, 1]
    make = []
    cnt = 0
    for i in ingredient:
        make.append(i)
        if make[-4:] == burger:
            cnt += 1
            del make[-4:]
    return cnt