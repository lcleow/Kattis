import sys
allin = sys.stdin.read().splitlines()
allin.pop(0)

for i, string in enumerate(allin):
    if i%2 == 0:
        print(string)