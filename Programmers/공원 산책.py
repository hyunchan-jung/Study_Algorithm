def get_next_location(n: int, current_location: tuple, direction: str) -> tuple:
    if direction == 'N':
        return (current_location[0] - n, current_location[1])
    elif direction == 'S':
        return (current_location[0] + n, current_location[1])
    elif direction == 'E':
        return (current_location[0], current_location[1] + n)
    elif direction == 'W':
        return (current_location[0], current_location[1] - n)
    else:
        raise ValueError('Invalid direction')


def solution(park, routes):
    locations = {}
    for row, p in enumerate(park):
        for col, value in enumerate(p):
            locations[(row, col)] = value
            if value == 'S':
                start = (row, col)

    for route in routes:
        direction, move = route.split(' ')

        is_movable = True
        for n in range(1, int(move) + 1):
            next_location = get_next_location(n, start, direction)
            if next_location not in locations:
                is_movable = False
                break
            elif locations[next_location] == 'X':
                is_movable = False
                break
        if is_movable:
            start = next_location

    return list(start)
