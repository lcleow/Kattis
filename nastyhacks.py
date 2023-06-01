import sys
allin = sys.stdin.read().splitlines()
allin.pop(0)

for line in allin:
    a, b, c = line.split()
    if int(a) < int(b) - int(c):
        print('advertise')
    elif int(a) == int(b) - int(c):
        print('does not matter')
    else:
        print('do not advertise')