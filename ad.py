import os
import sys

def template(year: str, day: str):
    return f"""
def pt1():
    with open('./{year}/{day}.txt') as f:
        lines = f.read().splitlines()
        print(lines)

def pt2():
    with open('./{year}/{day}.txt') as f:
        lines = f.read().splitlines()
        print(lines)

pt1()
# pt2()
"""

def main():
    args = sys.argv
    if len(args) < 3:
        print("Not enough arguments!")
        return
    year = args[1]
    day = args[2]
    if not year.isdigit():
        print("Year argument is not a valid number")
    if not day.isdigit():
        print("Day argument is not a valid number")
    if len(day) < 2:
        day = '0' + day
    day = 'd' + day
    txt = template(year, day)
    path = f"./{year}/{day}"
    path_py = path + '.py'
    path_txt = path + '.txt'
    if not os.path.isdir(year):
        os.makedirs(year)
    if os.path.isfile(path_py):
        print("File already exists!")
        return
    with open(path_py, 'w') as f:
        f.write(txt)
    with open(path_txt, 'w') as f:
        f.write("")

if __name__ == "__main__":
    main()