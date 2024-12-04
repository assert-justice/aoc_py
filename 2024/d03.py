
def is_digit(c):
    return '1234567890'.i

def parse(txt: str):
    idx = 0
    t = 0
    enable = True
    while True:
        idx = txt.find('mul(', idx)
        # print(txt[idx:])
        if idx == -1:
            break
        idx += 4
        comma = txt.find(',', idx)
        if comma == -1:
            continue
        x = txt[idx:comma]
        if not x.isdecimal():
            continue
        idx = comma + 1
        paren = txt.find(')', idx)
        if paren == -1:
            continue
        y = txt[idx:paren]
        if not y.isdecimal():
            continue
        t += int(x)*int(y)
    print(t)

def parse2(txt: str):
    start = 0
    current = 0
    total = 0
    enabled = True
    def at_eof() -> bool:
        return current >= len(txt)
    def peek() -> str:
        return txt[current]
    def advance() -> str:
        nonlocal current
        v = peek()
        current += 1
        return v
    def match(word: str) -> bool:
        nonlocal current
        for c in word:
            if c != peek():
                current = start
                return False
            advance()
        return True
    def mul() -> bool:
        nonlocal total
        if not match('mul('):
            return False
        comma = txt.find(',', current)
        if comma == -1:
            return False
        x = txt[current:comma]
        if not x.isdecimal():
            return False
        # print('mul', x)
        paren = txt.find(')', comma)
        if paren == -1:
            return False
        y = txt[comma+1:paren]
        if not y.isdecimal():
            return False
        print(f'mul({x}, {y})')
        if enabled:
            total += int(x)*int(y)
        return True
    while not at_eof():
        start = current
        if match('do()'):
            enabled = True
            print('do()')
        elif match('don\'t()'):
            enabled = False
            print('don\'t()')
        elif mul():
            pass
        else:
            advance()
    print('total:', total)

def pt1():
    with open('./2024/d03.txt') as f:
        line = f.read()
        parse(line)

def pt2():
    with open('./2024/d03.txt') as f:
        line = f.read()
        parse2(line)

# pt1()
pt2()
