
input = 'input.txt'
position = 50
clicks = 0

with open(input) as f:
    for line in f:
        sign = -1 if line[0] == 'L' else 1
        position += sign * int(line[1:])
        position %= 100
        if position == 0:
            clicks+=1

print(clicks)
