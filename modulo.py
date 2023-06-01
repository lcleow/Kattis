import sys
sampleinput = sys.stdin.read().splitlines()

modulo = [int(x)%42 for x in sampleinput if int(x)%42 >= 1 or int(x)%42 == 0]
unique = []
for x in modulo:
    if x not in unique:
        unique.append(x)
        
print(len(unique))