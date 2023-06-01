import sys
tempin = sys.stdin.read().split('\n')

negtemp = [x for x in tempin[1].split() if int(x)<0]
print(len(negtemp))