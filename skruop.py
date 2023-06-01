import sys
volchange = sys.stdin.read().splitlines()
volchange.pop(0)

start = 7
for x in volchange:
    if x == 'Skru op!':
        start += 1
        if start > 10:
            start = 10
    else:
        start -= 1
        if start < 0:
            start = 0

print(start)