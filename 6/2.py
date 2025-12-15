from functools import reduce
with open('input.txt') as f:
    data = list(
        map(
            lambda line: list(line), 
            f.read().split('\n')
        )
    )
    sum = 0
    transposed = [[row[i] for row in data] for i in range(len(data[0]))]
    i = len(transposed) - 1
    while i >= 0:
        numbers = []
        op = ''
        while len(list(filter(lambda c: c.strip() != '', transposed[i]))) != 0 and i>=0:
            num = int(''.join(transposed[i][:-1]))
            numbers.append(num)
            if transposed[i][-1] != ' ':
                op = transposed[i][-1]
            i-=1
        sub_sum = 0
        if op == '*':
            sub_sum = reduce(lambda x, y: x*y, numbers)
        elif op == '+':
            sub_sum = reduce(lambda x, y: x+y, numbers)
        sum += sub_sum
        i-=1
    print(sum)

    