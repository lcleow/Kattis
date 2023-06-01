string = input()
for i, x in enumerate(string):
    if x==')':
        if i-1 >= 0:
            if string[i-1]=='-':
                if i-2 >= 0:
                    if string[i-2]==':' or string[i-2]==';':
                        print(i-2)
            elif string[i-1]==':' or string[i-1]==';':
                print(i-1)