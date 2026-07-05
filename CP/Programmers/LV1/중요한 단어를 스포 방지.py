from collections import defaultdict

def solution(message, spoiler_ranges):
    n = len(message)
    c_list = []
    c_len = []
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        j = i
        while j < n and message[j] != ' ':
            j += 1
        c_list.append(message[i:j])
        c_len.append([i, j - 1])
        i = j
    blind_idx = set()
    for start, end in spoiler_ranges:
        for i, (len_s, len_e) in enumerate(c_len):
            if not (len_e < start or end < len_s):
                blind_idx.add(i)
    no_blind = set()
    for i, c in enumerate(c_list):
        if i not in blind_idx: no_blind.add(c)
    reveal_time = {}
    for i in blind_idx:
        len_s, len_e = c_len[i]
        over = []
        for idx, (start, end) in enumerate(spoiler_ranges):
            if not (len_e < start or end < len_s):
                over.append(idx)
        reveal_time[i] = max(over)
    reveal_groups = defaultdict(list)
    for i, rt in reveal_time.items():
        reveal_groups[rt].append(i)
    used = set()
    cnt = 0
    for rt in range(len(spoiler_ranges)):
        idxs = sorted(reveal_groups.get(rt, []))
        for i in idxs:
            text = c_list[i]
            if text in no_blind:      
                continue
            if text in used:          
                continue
            cnt += 1
            used.add(text)
    return cnt