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

with open("input.txt") as f:
    sum = 0
    map = f.read().split("\n")
    N = len(map)
    M = len(map[0])
    for i in range(N):
        for j in range(M):
            if map[i][j] == '@':
                if count_around(i, j, map, "@") < 4:
                    sum+=1
    print(sum)
