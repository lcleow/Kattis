n = int(input())
list1 = [int(x) for x in input().split()]
num = 0
for strike in list1:
    if strike == -1:
        n -= 1
    else:
        num += strike

print(num/n)