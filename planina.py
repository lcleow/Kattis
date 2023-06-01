import math
dict1 = {}
def iter(x):
    if x == 0:
        square = 1
        dict1[x] = square
        out = 4
    else:
        while x-1 not in dict1:
            iter(x-1)
        square = dict1[x-1]*4
        dict1[x] = square
        out = 4 + (math.sqrt(square)-1)*2*2 + (square+1-math.sqrt(square)*2)

    return int(out)

print(iter(int(input())))