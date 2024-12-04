def parse(lines: list[str]):
    out = []
    for line in lines:
        name, line = line.split(' bags contain ')
        bags = []
        for bag in line.split(','):
            [n,a,b] = bag.strip().split(' ')[:3]
            # print(bag.split(' ')[:3])
            if n == 'no':
                continue
            bags.append((int(n), a + ' ' + b))
        out.append((name, bags))
    return out

def pt1():
    with open('./2020/d07.txt') as f:
        lines = f.read().splitlines()
        data = parse(lines)
        for d in data:
            print(d)

def pt2():
    with open('./2020/d07.txt') as f:
        lines = f.read().splitlines()
        print(lines)

pt1()
# pt2()
