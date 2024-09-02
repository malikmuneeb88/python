game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0],] 

def win(Current_game):
    for row in game:
        print(row)
        all_match = True
        for item in row:
            if item != row[0]:
                all_match = False
        if all_match:
            print("Winner!!!")

win(game)