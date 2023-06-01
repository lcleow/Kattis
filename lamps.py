import math
allinput = input().split()
eprice = int(allinput[1])
hr = int(allinput[0])

def cost_incan(day1):
    bulb1 = 1
    if (hr*day1)/1000 > 1:
        bulb1 = math.ceil((hr*day1)/1000)
    cost1 = (60*eprice*hr*day1)/100000 + 5*bulb1
    return cost1

def cost_low(day2):
    bulb2 = 1
    if (hr*day2)/8000 > 1:
        bulb2 = math.ceil((hr*day2)/8000)
    cost2 = (11*eprice*hr*day2)/100000 + 60*bulb2
    return cost2

count = 0
while cost_low(count) > cost_incan(count):
    count += 1

print(count)