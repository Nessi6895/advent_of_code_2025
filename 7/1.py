with open('input.txt') as f:
    data = list(map(lambda line: list(line), f.readlines()))
    splits = 0
    for i in range(1, len(data)):
        for j, ch in enumerate(data[i]):
            input = data[i-1][j]
            if input == 'S' or input == '|':
                if ch == '^':
                    splits+=1
                    data[i][j-1] = '|'
                    data[i][j+1] = '|'
                else:
                    data[i][j] = '|'
    # to print picture =)
    for line in data:
        print(''.join(line))
    print(splits)

