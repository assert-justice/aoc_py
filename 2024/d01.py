from collections import defaultdict

def pt1():
    with open('./2024/d01.txt') as f:
        txt = f.readlines()
        a = []
        b = []
        for line in txt:
            [a1,b1] = line.split('   ')
            a.append(int(a1))
            b.append(int(b1))
        a.sort()
        b.sort()
        # print(a)
        t = 0
        for x,y in list(zip(a,b)):
            t += abs(x-y)
        print(t)

def pt2():
    with open('./2024/d01.txt') as f:
        txt = f.read().splitlines()
        a = []
        b = defaultdict(lambda: 0)
        for line in txt:
            [a1,b1] = line.split('   ')
            a1 = int(a1)
            b1 = int(b1)
            a.append(a1)
            b[b1] += 1
        a.sort()
        # print(a)
        t = 0
        for x in a:
            t += x * b[x]
        print(t)
pt1()
pt2()