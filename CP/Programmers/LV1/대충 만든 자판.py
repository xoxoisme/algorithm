def solution(keymap, targets):
    def find_min(keymap, c):
        min_val=float('inf')
        for i in range(len(keymap)):
            if c in keymap[i]: min_val = min(min_val, keymap[i].index(c)+1)
        return min_val if min_val != float('inf') else -1
    res=[]
    for s in targets:
        cnt=0
        flg=True
        for c in s:
            val = find_min(keymap, c)
            if val == -1:
                flg = False
                break
            cnt+=val
        res.append(cnt if flg else -1)
    return res