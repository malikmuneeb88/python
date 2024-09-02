game = [[2, 0, 1],
        [2, 0, 0],
        [2, 2, 0],] 

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print ("winner!!") 
