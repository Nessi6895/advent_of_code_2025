ranges = []
ids = []
with open('input.txt') as f:
    mode = 0
    for line in f:
        if line == "\n":
            mode = 1
            continue
        if mode == 0:
            range = line.split("-")
            ranges.append((int(range[0]), int(range[1])))
        else:
            ids.append(int(line))
count = 0
for id in ids:
    for range in ranges:
        if id <= range[1] and id >= range[0]:
            count+=1
            break

print(count)