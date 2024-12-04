
def validate(line: list[int]):
    line = zip(line[:-1], line[1:])
    line = [(a-b) for a,b in line ]
    if line[0] < 0:
        line = [-n for n in line]
    for n in line:
        if n < 1 or n > 3:
            return False
    return True

def spam(line: list[int]) -> bool:
    if validate(line):
        return True
    for idx in range(len(line)):
        l = line[:]
        l.pop(idx)
        if validate(l):
            return True
    return False

def pt1():
    with open('./2024/d02.txt') as f:
        lines = f.read().splitlines()
        v = 0
        for line in lines:
            if validate([int(n) for n in line.split(' ')]):
                v += 1
        print(v)

def pt2():
    with open('./2024/d02.txt') as f:
        lines = f.read().splitlines()
        v = 0
        for line in lines:
            if spam([int(n) for n in line.split(' ')]):
                v += 1
        print(v)

pt1()
pt2()
