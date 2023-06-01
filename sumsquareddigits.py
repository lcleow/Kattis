def ssd(b, n):
    a = []
    power = 0
    while b**power <= n:
        power +=1
    for i in range(power-1, -1, -1):
        singlea = n//(b**i)
        a.append(singlea)
        n -= singlea*b**i
    s = 0
    for x in a:
        s += x**2
    return s

n = int(input())
for i in range(n):
    setno, b, n = map(int, input().split())
    print(setno, ssd(b, n))