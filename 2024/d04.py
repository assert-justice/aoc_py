
def count(lines: list[str]) -> int:
    xmas = 'XMAS'
    width = len(lines[0])
    height = len(lines)
    def on_grid(x: int, y: int) -> bool:
        if x < 0 or x >= width:
            return False
        if y < 0 or y >= height:
            return False
        return True
    def get(x: int, y: int) -> str:
        if not on_grid(x, y):
            return '.'
        l = lines[y]
        return l[x]
    def match(word: str, x: int, y: int, dx: int, dy: int) -> bool:
        for c in word:
            test = get(x, y)
            if test != c:
                return False
            x += dx
            y += dy
        return True
    total = 0
    for y in range(0, height):
        for x in range(0, width):
            if match(xmas, x, y, 1, 0):
                total += 1
            if match(xmas, x, y, 1, 1):
                total += 1
            if match(xmas, x, y, 0, 1):
                total += 1
            if match(xmas, x, y, -1, 1):
                total += 1
            if match(xmas, x, y, -1, 0):
                total += 1
            if match(xmas, x, y, -1, -1):
                total += 1
            if match(xmas, x, y, 0, -1):
                total += 1
            if match(xmas, x, y, 1, -1):
                total += 1
    print(total)

def count2(lines: list[str]) -> int:
    width = len(lines[0])
    height = len(lines)
    def on_grid(x: int, y: int) -> bool:
        if x < 0 or x >= width:
            return False
        if y < 0 or y >= height:
            return False
        return True
    def get(x: int, y: int) -> str:
        if not on_grid(x, y):
            return '.'
        l = lines[y]
        return l[x]
    def match(word: str, x: int, y: int, dx: int, dy: int) -> bool:
        for c in word:
            test = get(x, y)
            if test != c:
                return False
            x += dx
            y += dy
        return True
    total = 0
    for y in range(0, height):
        for x in range(0, width):
            if get(x, y) != 'A':
                continue
            a = match('MAS', x-1, y-1, 1, 1) or match('SAM', x-1, y-1, 1, 1)
            b = match('MAS', x-1, y+1, 1, -1) or match('SAM', x-1, y+1, 1, -1)
            if a and b:
                total += 1
    print(total)

def pt1():
    with open('./2024/d04.txt') as f:
        lines = f.read().splitlines()
        count(lines)

def pt2():
    with open('./2024/d04.txt') as f:
        lines = f.read().splitlines()
        count2(lines)

# pt1()
pt2()
