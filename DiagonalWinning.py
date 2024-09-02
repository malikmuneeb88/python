game = [[1, 0, 1],
        [2, 1, 0],
        [2, 2, 1],] 

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)

# if game[0][0] == game[1][1] == game[2][2]:
#     print("Winner!!")

# if game[2][0] == game[1][1] == game[0][2]:
#     print("Winner!!")
# '''