a, b, c = map(int, input().split())
if a-b >= b and a-c >= c:
    print((a-b)*(a-c)*4)
elif a-b >= b and a-c < c:
    print((a-b)*c*4)
elif a-b < b and a-c >= c:
    print(b*(a-c)*4)
else:
    print(b*c*4)