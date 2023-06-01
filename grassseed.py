import sys
allinput = sys.stdin.read().splitlines()
cost = float(allinput.pop(0))
allinput.pop(0)
totalcost = 0
for line in allinput:
    a, b = line.split()
    area = float(a)*float(b)
    totalcost += area*cost

print(f'{totalcost:.8f}')