import sys
allinput = sys.stdin.read().splitlines()
periods = allinput.pop(0)

qaly = 0
for lines in allinput:
    a, b = map(float, lines.split())
    qaly += a*b

print(qaly)