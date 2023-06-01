n = int(input())

def countplug(x):
    list1 = [int(a) for a in x]
    sump = 0
    for item in list1[1:]:
        sump += item - 1
    return sump + 1

for line in range(n):
    x = input().split()
    print(countplug(x))