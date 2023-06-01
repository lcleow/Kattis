import sys
number_in = sys.stdin.read().split('\n')
number_in.pop(0)
number_in.pop(-1)
final_sum = 0
for x in number_in:
    y = int(x[:-1]) ** int(x[-1])
    final_sum += y

print(final_sum)