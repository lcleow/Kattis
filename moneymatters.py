import sys
allinput = sys.stdin.read().splitlines()
firstline = allinput.pop(0)
human_no = int(firstline.split()[0])
friendship_no = int(firstline.split()[1])
account = allinput[:human_no]

bank = {}
for i in range(human_no):
    bank[i] = int(account[i])

friends = {}
for i in range(human_no):
    friends[i] = [i]

relations = allinput[human_no:]
for relation in relations:
    rel_list = [int(x) for x in relation.split()]
    friends[rel_list[0]].append(rel_list[1])
    friends[rel_list[1]].append(rel_list[0])

def groupfriends(x):
    y = []
    y.extend(x)
    for human in x:
        y.extend(friends[human])
    y = list(set(y))
    return y

def loopgroup(x):
    prevlist = x
    while True:
        newlist = groupfriends(prevlist)
        if len(newlist) == len(prevlist):
            return newlist
        else:
            prevlist = newlist
    
def dropfriend(x):
    focus = x
    for item in focus:
        friends.pop(item)
        dictkeys.remove(item)

finallist = []
dictkeys = list(friends.keys())
while len(friends) > 0:
    newlist = loopgroup(friends[dictkeys[0]])
    finallist.append(newlist)
    dropfriend(newlist)
    
transactions = []
for connection in finallist:
    transfer = sum([bank[human] for human in connection])
    transactions.append(transfer)

if max(transactions) == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')