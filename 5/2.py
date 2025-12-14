def intersect(r1, r2):
    left_overlap = r2[0] <= r1[1] and r2[1] >= r1[1]
    right_overlap = r1[0] <= r2[1] and r1[1] >= r2[1]
    return left_overlap or right_overlap

ranges = []
with open('input.txt') as f:
    for line in f:
        if line == "\n":
            break
        split = line.split("-")
        ranges.append((int(split[0]), int(split[1])))

ranges_with_redundancy = list(map(lambda r: (r[0], r[1], True), ranges))
is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(1,len(ranges_with_redundancy)):
        r1 = ranges_with_redundancy[i]
        if not r1[2]:
            continue
        for j in range(0,i):
            r2 = ranges_with_redundancy[j]
            if not r2[2]:
                continue
            if intersect(r1, r2):
                ranges_with_redundancy[j] = (min(r1[0], r2[0]), max(r1[1], r2[1]), True)
                ranges_with_redundancy[i] = (r1[0], r1[1], False)
                is_sorted = False
                break
sum=0
for r in ranges_with_redundancy:
    if r[2]:
        sum+=r[1]-r[0]+1
print(sum)
