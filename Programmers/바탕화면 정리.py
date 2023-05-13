def solution(wallpaper):
    locations = []
    for y, line in enumerate(wallpaper, 0):
        line = list(line)
        for _ in range(line.count('#')):
            x = line.index('#')
            locations.append((x, y))
            line[x] = '.'

    xtl = min(locations, key=lambda x: x[0])[0]
    ytl = min(locations, key=lambda x: x[1])[1]
    xbr = max(locations, key=lambda x: x[0])[0] + 1
    ybr = max(locations, key=lambda x: x[1])[1] + 1
    answer = [ytl, xtl, ybr, xbr]

    return answer
