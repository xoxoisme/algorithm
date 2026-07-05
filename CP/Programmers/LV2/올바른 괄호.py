def solution(s):
    ls = list(s)
    stack = []
    for c in ls:
        stack.append(c)
        if stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()
    if stack == []: return True
    return False