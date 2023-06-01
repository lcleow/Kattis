import sys
import math

ringsize = sys.stdin.read().splitlines()
ringsize.pop(0)
sizelist = ringsize[0].split()
firstring = int(sizelist.pop(0))


for x in sizelist:
    gcden = math.gcd(firstring, int(x))
    if gcden == int(x):
        print(f'{firstring/int(x):.0f}/1')
    elif gcden > 1:
        print(f'{firstring/gcden:.0f}/{int(x)/gcden:.0f}')
    else:
        print(f'{firstring}/{x}')