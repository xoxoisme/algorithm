def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        if stack[-2:] == stack[-1:]*2:
            stack.pop()
            stack.pop()
    if len(stack) == 0: return 1
    return 0