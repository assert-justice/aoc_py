
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

def match(txt: str, idx: int):
    ss = ['mul(', 'do()', 'don\'t()']
    id = 0
    for s in ss:
        f = txt.find(s, idx)
        if f == -1:
            continue
    

def parse2(txt: str):
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
        if enable:
            t += int(x)*int(y)
    print(t)

def pt1():
    with open('./2024/d03.txt') as f:
        line = f.read()
        parse(line)

def pt2():
    with open('./2024/d03.txt') as f:
        line = f.read()
        parse2(line)

pt1()
# pt2()
