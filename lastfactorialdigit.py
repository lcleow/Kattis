import sys
allin = sys.stdin.read().splitlines()
allin.pop(0)

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1)*n

for x in allin:
    print(factorial(int(x))%10)