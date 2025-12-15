with open('input.txt') as f:
    data = list(
        map(
            lambda line: list(filter(lambda s: s!='', map(lambda s: s.strip(), line.split(' ')))), 
            f.read().split('\n')
        )
    )
    print(len(data))
    sum = 0
    for i in range(len(data[0])):
        n0 =int(data[0][i])
        n1 = int(data[1][i])
        n2 = int(data[2][i])
        n3 = int(data[3][i])
        op = data[4][i]
        result = 0 
        if op == '*':
            result=n0*n1*n2*n3
        else:
            result=n0+n1+n2+n3
        if result < 0:
            print("FUCK")
        sum+=result
    print(sum)

    