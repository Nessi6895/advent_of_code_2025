with open("input.txt") as f:
    sum = 0
    for line in f:
        rack = list(map(lambda ch: int(ch), line.strip()))
        l_ptr = 0
        rack_sum = 0
        for i in range(12):
            r_ptr = len(rack) - 11 + i
            pi = r_ptr-1
            di = rack[pi]
            for bi, b in enumerate(reversed(rack[l_ptr:r_ptr])):
                if b >= di:
                    normalized_ind = r_ptr-bi-1
                    di = b
                    pi = normalized_ind
            l_ptr = pi+1
            rack_sum += di * 10**(11-i)
        sum+=rack_sum
    print(sum)
