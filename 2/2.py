import sys

# number of digits    
def nod(x):
    n = 0
    while x != 0:
        x=int(x/10)
        n+=1
    return n

# is number funny
def funny(x):
    d = nod(x)
    if d <= 1:
        return False
    fs = sorted(factors(d))
    if len(fs) == 1:
        tmp = x // 10
        last = x % 10
        while tmp > 0:
            if last != tmp % 10:
                return False
            tmp = tmp // 10
        return True
    for f in fs[1:]:
        base = x%10**f
        tmp = x//(10**f)
        while tmp > 0:
            next = tmp%(10**f)
            if next != base:
                break
            else:
                tmp = tmp//(10**f)
                if tmp == 0:
                    return True
    return False
            
# nearest right funny number
def nrfn(x):
    d = nod(x)
    if d <= 1:
        return 11
    biggest_possible = 10**d - 1
    if x == biggest_possible:
        next_d = d+1
        fs = sorted(factors(next_d))
        if len(fs) <= 1:
            return int("1"*next_d)
        f = next_d//fs[1]
        print(f)
        base = str(10**next_d)[:f]
        res = int(base*(next_d//f))
        return res
    nearest = biggest_possible
    for f in factors(d):
        level = int(str(x)[:f])
        tmp = str(x)[f:]
        while tmp != "":
            next = int(str(tmp)[:f])
            if level > next:
                break
            elif level < next:
                level+=1
                break
            else:
                tmp = tmp[f:]
                if tmp == "":
                    level+=1
        number = int(str(level)*(int(d/f)))
        if number < nearest:
            nearest = number
    return nearest
    
def factors(n: int):
    if n <= 0:
        return []
    divisors = []
    to = int(n**0.5 + 1)
    for i in range(1, to):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and i != 1:
                divisors.append(n // i)
    return divisors

def loop(start, end, sum = 0):
    while start <= end:
        print(start)
        sum+=start
        start = nrfn(start)
    return sum

# sum of funny numbers on range
def sum_funny(start, end):
    if funny(start):
        return loop(start, end)
    return loop(nrfn(start), end)


file = "input.txt"
ranges = []
with open(file) as f:
    for r in f.read().split(","):
        split = r.split("-")
        ranges.append((int(split[0]), int(split[1])))

sum = 0
for id, r in enumerate(ranges):
    sum+=sum_funny(r[0], r[1])
print(sum)



