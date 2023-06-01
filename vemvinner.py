def hori(mat1):
    result = 0
    for row in mat1:
        if all(play == row[0] for play in row):
            if row[0] != '_':
                result = row[0]
    return result

def vert(mat1):
    result = 0
    for i in range(3):
        if all(mat1[j][i]==mat1[0][i] for j in range(3)):
            if mat1[0][i] != '_':
                result = mat1[0][i]
    return result

def diag(mat1):
    list1 = []
    list2 = []
    for i in range(3):
        list1.append(mat1[i][i])
        list2.append(mat1[i][2-i])
    if all(x==list1[0] for x in list1):
        return list1[0]
    if all(y==list2[0] for y in list2):
        return list2[0]
    return 0
        
def win(mat1):
    list3 = [hori, vert, diag]
    for wincon in list3:
        if wincon(mat1):
            return wincon(mat1)
    return 0
    
def main():
    players = {'X': 'Johan', 'O': 'Abdullah'}
    matrix = [input().split() for i in range(3)]
    if win(matrix) in players:
        return f'{players[win(matrix)]} har vunnit'
    else:
        return 'ingen har vunnit'
    
if __name__ == '__main__':
    print(main())