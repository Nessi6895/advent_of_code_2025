from asyncio import to_thread


def count_around(x, y, map, candidate):
    N = len(map)
    M = len(map[0])
    sum=0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i==x and j==y) and i>=0 and i<N and j>=0 and j<M:
                if map[i][j] == candidate:
                    sum+=1
    return sum

def mark_to_remove(map: list[list[str]]):
    N = len(map)
    M = len(map[0])
    to_remove = []
    for i in range(N):
        for j in range(M):
            if map[i][j] == '@' and count_around(i, j, map, '@') < 4:
                to_remove.append((i, j))
    return to_remove

with open("input.txt") as f:
    sum = 0
    map = list(map(lambda line: list(line), f.read().split("\n")))
    N = len(map)
    M = len(map[0])
    to_remove = mark_to_remove(map)
    while len(to_remove) > 0:
        sum+=len(to_remove)
        for coords in to_remove:
            map[coords[0]][coords[1]] = '.'
        to_remove = mark_to_remove(map)
    print(sum)
