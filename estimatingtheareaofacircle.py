import sys
import math

circles = sys.stdin.read().splitlines()
circles.pop()

for line in circles:
    list1 = line.split()
    area = math.pi*(float(list1[0])**2)
    estimated = ((2*float(list1[0]))**2) * int(list1[2])/int(list1[1])
    print(f'{area} {estimated}')
