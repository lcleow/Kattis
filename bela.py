import sys
hand_input = sys.stdin.read().split('\n')
hand_input.pop()
firstline = hand_input.pop(0).split()
trump = firstline[1]

dom_dic = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
non_dic = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
output = 0

for x in hand_input:
    if x[-1] == trump:
        value = dom_dic[x[0]]
    else:
        value = non_dic[x[0]]
    output += value

print(output)