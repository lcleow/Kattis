import sys
numbers = sys.stdin.read().splitlines()
numbers.pop(0)

for x in numbers[::-1]:
    print(x)