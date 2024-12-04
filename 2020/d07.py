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
        lookup = {}
        for name,bags in data:
            l = []
            for _,b in bags:
                l.append(b)
            lookup[name] = l
        def contains(name: str) -> bool:
            l = lookup[name]
            if 'shiny gold' in l:
                return True
            for n in l:
                if contains(n):
                    return True
            return False
        total = 0
        # print(contains('faded blue'))
        for name in lookup.keys():
            if contains(name):
                total += 1
        print(total)

def pt2():
    with open('./2020/d07.txt') as f:
        lines = f.read().splitlines()
        data = parse(lines)
        mem = {}
        lookup = {}
        for name,bags in data:
            lookup[name] = bags
        def count(name: str) -> int:
            if name in mem:
                return mem[name]
            total = 0
            for c,n in lookup[name]:
                total += c * count(n) + c
            mem[name] = total
            return total
        print(count('shiny gold'))
        

# pt1()
pt2()
