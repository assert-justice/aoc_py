from time import time

def timer_func(func): 
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func 

def solve(lines: list[str]):
    width = len(lines[0])
    height = len(lines)
    solid = set()
    visited = set()
    dirs = [(0,-1,), (1,0,), (0,1,), (-1,0,)]
    dir_idx = 0
    gx = 0
    gy = 0
    def is_solid(x: int, y: int) -> bool:
        return (x, y,) in solid
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == '.':
                continue
            elif c == '#':
                solid.add((x,y,))
            else:
                gx = x
                gy = y
    # patrol
    while True:
        if gx < 0 or gx >= width:
            break
        elif gy < 0 or gy >= height:
            break
        visited.add((gx, gy,))
        x = gx
        y = gy
        # try to move in direction
        x += dirs[dir_idx][0]
        y += dirs[dir_idx][1]
        if is_solid(x, y):
            dir_idx += 1
            if dir_idx > 3:
                dir_idx = 0
        else:
            gx = x
            gy = y
    print(len(visited))

def solve2(lines: list[str]):
    width = len(lines[0])
    height = len(lines)
    solid = set()
    # visited = set()
    dirs = [(0,-1,), (1,0,), (0,1,), (-1,0,)]
    # dir_idx = 0
    gx = 0
    gy = 0
    def is_solid(x: int, y: int) -> bool:
        return (x, y,) in solid
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == '.':
                continue
            elif c == '#':
                solid.add((x,y,))
            else:
                gx = x
                gy = y
    # patrol
    def does_patrol_loop(gx: int, gy: int, sx: int, sy: int) -> bool:
        visited = set()
        dir_idx = 0
        while True:
            if gx < 0 or gx >= width:
                return False
            elif gy < 0 or gy >= height:
                return False
            pos = (gx, gy, dir_idx,)
            if pos in visited:
                return True
            visited.add(pos)
            x = gx
            y = gy
            # try to move in direction
            x += dirs[dir_idx][0]
            y += dirs[dir_idx][1]
            if is_solid(x, y) or (x == sx and y == sy):
                dir_idx += 1
                if dir_idx > 3:
                    dir_idx = 0
            else:
                gx = x
                gy = y
    tally = 0
    for x in range(width):
        for y in range(height):
            if is_solid(x,y):
                continue
            if gx == x and gy == y:
                continue
            if does_patrol_loop(gx, gy, x, y):
                tally += 1
    print(tally)

def pt1():
    with open('./2024/d06.txt') as f:
        lines = f.read().splitlines()
        solve(lines)

@timer_func
def pt2():
    with open('./2024/d06.txt') as f:
        lines = f.read().splitlines()
        solve2(lines)

# pt1()
pt2()
