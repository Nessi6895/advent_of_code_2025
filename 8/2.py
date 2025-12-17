points = []

class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"P({self.x}, {self.y}, {self.z})"

def distance(a: Point, b: Point):
    return ((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)**0.5

with open('input.txt') as f:
    for line in f:
        split = line.split(',')
        points.append(Point(int(split[0]), int(split[1]), int(split[2])))

distances = []

for i, a in enumerate(points):
    for j, b in enumerate(points[i+1:]):
        d = distance(a, b)
        distances.append((d, (i, i+j+1)))

nets: list[set[int]] = []

# prefill network
for i, _ in enumerate(points):
    nets.append({i})

all_connections: list[tuple[int, int]] = list(map(lambda d: d[1], sorted(distances, key=lambda d: d[0])))

for a, b in all_connections:
    a_was_in: set[int] = set()
    b_was_in: set[int] = set()
    for net in nets:
        if a in net:
            a_was_in = net
        if b in net:
            b_was_in = net
        if len(a_was_in) > 0 and len(b_was_in) > 0:
            break
    if a_was_in != b_was_in:
        nets.remove(a_was_in)
        nets.remove(b_was_in)
        nets.append(a_was_in.union(b_was_in))
    if len(nets) == 1:
        print(points[a].x*points[b].x)
        break
