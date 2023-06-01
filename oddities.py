import sys
allinput = sys.stdin.read().splitlines()
allinput.pop(0)

for integer in allinput:
    if int(integer) % 2 == 0:
        evenodd = 'even'
    else:
        evenodd = 'odd'
    print(f'{integer} is {evenodd}')