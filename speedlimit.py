import sys
allinput = sys.stdin.read().splitlines()

setposition = []
for i, x in enumerate(allinput):
    if len(x) <= 2:
        setposition.append(i)

for j, y in enumerate(setposition):
    if allinput[y] == '-1':
        break
    inputset = allinput[(y+1):(setposition[j+1])]
    inputsum = 0
    prevb = 0
    for row in inputset:
        a, b = row.split()
        inputsum += int(a)*(int(b) - prevb)
        prevb = int(b)
    print(f'{inputsum} miles')