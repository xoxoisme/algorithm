def solution(numbers, hand):
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    def find_pos(k):
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                if keypad[i][j] == k:
                    return (i, j)
    def dsts(hand, target):
        return abs(target[0]-hand[0])+abs(target[1]-hand[1])
    res = []
    l, r = find_pos('*'), find_pos('#')
    for n in numbers:
        target = find_pos(str(n))
        if n in (1, 4, 7):
            res.append('L')
            l = target
        elif n in (3, 6, 9):
            res.append('R')
            r = target
        else:
            dl = dsts(l, target)
            dr = dsts(r, target)
            
            if dl < dr:
                res.append('L')
                l = target
            elif dl > dr:
                res.append('R')
                r = target
            else:
                if hand == 'left':
                    res.append('L')
                    l = target
                elif hand == 'right':
                    res.append('R')
                    r = target
    return ''.join(res)