from collections import defaultdict

def parse(lines: list[str]):
    ordering = []
    updates = []
    phase = 0
    for line in lines:
        if line == '':
            phase = 1
        elif phase == 0:
            ordering.append(tuple([int(n) for n in line.split('|')]))
        else:
            updates.append([int(n) for n in line.split(',')])
    return (ordering, updates,)
        

def solve():
    with open('./2024/d05.txt') as f:
        lines = f.read().splitlines()
        ordering, updates = parse(lines)
        # print(ordering)
        # print(updates)
        lookup = defaultdict(list)
        for a,b in ordering:
            lookup[b].append(a)
        def valid(update: list[int]) -> bool:
            # print(update)
            l = []
            for u in update:
                if u in lookup:
                    for req in lookup[u]:
                        # print(u, req)
                        if req in update and not req in l:
                            return False
                l.append(u)
            return True
        def correct(idx: int, update: list[int]) -> bool:
            up = update[:idx]
            val = update[idx]
            if not val in lookup:
                return True
            req = lookup[val]
            for r in req:
                if r in update and not r in up:
                    return False
            return True
        def fix(update: list[int], start: int = 0) -> list[int]:
            update = update[:]
            # print(update)
            for idx in range(start, len(update)-1):
                if not correct(idx, update):
                    # print(update, update[idx])
                    # break
                    update[idx],update[idx+1] = update[idx+1],update[idx]
                    update = fix(update, idx+1)
                    return fix(update)
            return update
        total = 0
        fixed = 0
        for up in updates:
            if valid(up):
                l = len(up)
                assert l % 2 == 1
                total += up[l//2]
            else:
                up = fix(up)
                l = len(up)
                fixed += up[l//2]
                # print(up)
        print("valid:", total)
        print("fixed:", fixed)

solve()
