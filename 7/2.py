from ast import Dict


data = []

cache: dict[tuple[int, int], int] = {}

def timelines_from_point(x, y):
    global cache
    global data
    if x<0 or x >= len(data) or y<0 or y>=len(data[x]):
        return 0
    if (x, y) in cache:
        return cache.get((x, y))
    if data[x][y] == '^':
        result = 1+timelines_from_point(x+1, y+1) + timelines_from_point(x+1, y-1)
        cache[(x, y)] = result
        return result
    else:
        result = timelines_from_point(x+1, y)
        cache[(x, y)] = result
        return result

with open('input.txt') as f:
    data = list(map(lambda line: list(line), f.readlines()))
    for i, ch in enumerate(data[0]):
        if ch == 'S':
            result = 1 + timelines_from_point(0, i)
            print(result)
            break
