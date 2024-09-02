game_size = 3

print("   0  1  2")

s = " "
for i in range(game_size):
    s += "  "+str(i)

# print(s)

s = "   "+"  ".join([str(i) for i in range(game_size)])

print(s)


dictionaries = {"Key1":15, "Key2":32}

print(dictionaries["Key1"])

dictionaries["HiThere"] = 92

print(dictionaries)




game_size = 5 

'''
game = []

for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
    game.append(row)
'''

game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)

