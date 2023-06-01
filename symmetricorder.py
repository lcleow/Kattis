import sys
allinput = sys.stdin.read().splitlines()
first = int(allinput.pop(0))

def sortorder(a, b):
    setn = allinput[a:b]
    for i, item in enumerate(setn):
        if i%2 == 0:
            print(item)
    oddindex = []
    for i, item in enumerate(setn):
        if i%2 == 1:
            oddindex.append(item)
    for name in oddindex[::-1]:
        print(name)

def nosets(first, allinput):
    start = 0
    end = first
    setno = [[start, end]]
    while end != len(allinput)-1:
        start = end+1
        end += int(allinput[end])+1
        setno.append([start, end])
    return setno

number = 1
for sets in nosets(first, allinput):
    a, b = sets
    print(f'SET {number}')
    number += 1
    sortorder(a, b)