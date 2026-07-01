def solution(wallpaper):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_x, min_y = min(i, min_x), min(j, min_y)
                max_x, max_y = max(i+1, max_x), max(j+1, max_y)
    return [min_x, min_y, max_x, max_y]