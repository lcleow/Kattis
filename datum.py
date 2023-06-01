import datetime as dt
d, m = map(int, input().split())
day = dt.date(2009, m, d).strftime('%A')
print(day)