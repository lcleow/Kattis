import sys
allinput = sys.stdin.read().splitlines()
game_no = allinput.count('right on')
game_dict = {}
remain = allinput.copy()
for i in range(game_no):
    game_dict[i] = remain[:(remain.index('right on')+1)]
    remain = remain[(remain.index('right on')+1):]
game_target = []
for game in game_dict:
    game_target.append(int(game_dict[game][-2]))


def resolvegame(res1, target):
    numbers = res1[:-2:2]
    answers = res1[1:-2:2]
    check = 0
    for num, ans in zip(numbers, answers):
        if ans == 'too high':
            if int(num) <= target:
                check += 1
        elif ans == 'too low':
            if int(num) >= target:
                check += 1
        if check != 0:
            return 'Stan is dishonest'
    return 'Stan may be honest'

for game in game_dict:
    print(resolvegame(game_dict[game], game_target[game]))