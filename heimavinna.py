line = input()
def seq(a):
    num = a.split('-')
    return int(num[-1]) - int(num[0]) + 1

if ';' in line:
    line = line.split(';')
else:
    line = [line]

count = 0
for i in line:
    if '-' in i:
        count += seq(i)
    else:
        count += 1

print(count)