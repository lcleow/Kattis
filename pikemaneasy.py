def main():
    n, t = map(int, input().split())
    a, b, c, t0 = map(int, input().split())
    timelist = [t0]
    for x in range(1, n):
        timelist.append((a*timelist[x-1]+b)%c + 1)
    problems, penalty = calctime(t, sorted(timelist))
    print(problems, penalty)
    
def calctime(t, timelist):
    totalt, penalty, problems = 0, 0, 0
    for item in timelist:
        if totalt + item > t:
            return problems, penalty
        totalt += item
        problems += 1
        penalty = (penalty + totalt)%1000000007
    return problems, penalty

main()