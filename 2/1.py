import math

# number of digits    
def nod(x):
    n = 0
    while x != 0:
        x=int(x/10)
        n+=1
    return n

# is this number funny
def funny(x):
    if idz(x):
        return False
    half_order = int(nod(x)/2)
    first_half = int(x / math.pow(10, half_order))
    second_half = x % (half_order*10)
    return second_half == first_half

# nearest right funny number
def nrfn(x):
    if idz(x):
        return lfnoo(nod(x)+1)
    half_order = int(nod(x)/2)
    first_half = int(x / math.pow(10, half_order))
    second_half = int(x % (math.pow(10, half_order)))
    # 89, 9899, 998999, and so on
    if first_half == second_half and second_half == int(math.pow(10, half_order))-1:
        return lfnoo(nod(x)+2)
    elif first_half > second_half:
        next_first_half = first_half
    else:
        next_first_half = first_half+1
    return int(next_first_half * math.pow(10, half_order) + next_first_half)

# is point in the deadzone
def idz(x):
    return nod(x)%2==1
    
# nearest number of higher order
def nnoho(x):
    d = nod(x)
    return int(math.pow(10, d))
    
# lowest funny number of order
def lfnoo(order):
    if order%2 != 0:
        return None
    half_order = int(order/2)
    half_num = int(math.pow(10, half_order-1))
    return half_num * half_num * 10 + half_num
    
def loop(start, end, sum = 0):
    while start <= end:
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
    for range in f.read().split(","):
        split = range.split("-")
        ranges.append((int(split[0]), int(split[1])))

sum = 0
for range in ranges:
    sum+=sum_funny(range[0], range[1])
print(sum)

