chessinput = [int(x) for x in input().split()]
chesspiece = [1, 1, 2, 2, 2, 8]

chessoutput = ''
for i, x in enumerate(chessinput):
    chessoutput += str(chesspiece[i] - x) + " "

print(chessoutput)
    