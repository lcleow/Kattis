def remain(x):
    cap = (x[0] - x[1])*0.9
    return cap

def itemweight(y):
    total = 0
    for item in y:
        total += item
    return total

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(round((remain(x) - itemweight(y))))