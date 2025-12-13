with open("input.txt") as f:
    sum = 0
    for line in f:
        rack = list(map(lambda ch: int(ch), line.strip()))
        l = rack[-2]
        li = len(rack)-1
        for ind, b in enumerate(reversed(rack[:len(rack)-1])):
            if b >= l:
                l = b
                li = len(rack) - ind - 2
        r = max(rack[li+1:])
        sum+=l*10+r
    print(sum)
