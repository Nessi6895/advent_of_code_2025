import math

input = input.txt
position = 50
clicks = 0

with open(input) as f:
    for line in f:
        start = position
        sign = -1 if line[0] == L else 1
        offset = int(line[1:])
        if offset == 0:
            break
        before_normalization = position + sign * offset
        position = before_normalization % 100
        clicks += abs(math.floor(before_normalization / 100))
        if start != 0 and position == 0 and before_normalization <= 0:
            clicks+=1
        if start == 0 and position != 0 and before_normalization < 0:
            clicks-=1
print(clicks)
