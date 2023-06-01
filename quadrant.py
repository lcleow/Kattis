import sys
x, y = sys.stdin.read().splitlines()

if int(x) > 0:
    if int(y) > 0:
        print(1)
    elif int(y) < 0:
        print(4)
elif int(x) < 0:
    if int(y) > 0:
        print(2)
    elif int(y) < 0:
        print(3)