n = int(input()) 

def candles(x):
    first = 2
    last = first + x - 1
    return ((first+last)/2) * x

for line in range(1, n+1):
    a, b = map(int, input().split())
    print(a, int(candles(b)))