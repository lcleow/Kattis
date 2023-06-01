allinput = input().split()
int1 = int(allinput[0])
int2 = int(allinput[1])
total = int(allinput[2])

for i in range(total):
    if (i+1)%int1 == 0 and (i+1)%int2 == 0:
        print('FizzBuzz')
    elif (i+1)%int1 == 0:
        print('Fizz')
    elif (i+1)%int2 == 0:
        print('Buzz')
    else:
        print(i+1)