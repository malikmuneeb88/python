#Q1: Read then text from a given file 'poems.txt' and find out whether it contains the word 'Twinkle'.
# file = open('poems.txt')
# t = file.read()

# if 'Twinkle' in t:
#     print("Twinkle is present in t")

# else:
#     print("Twinkle is not present in t")
# file.close()




#Q2: The game() function in a program lets a user play a game and returns the score as aninteger. You need to read a file 'HiScore.txt' which is either blank or contains the previous Hi-score. Update the Hi-score whenener game() breaks the Hi-Score. 
# def game():
#     return 3453

# score = game()
# with open("HiScore.txt") as f:
#     HiScoreStr = f.read()

# if HiScoreStr == '':
#     with open("HiScore.txt", "w") as f:
#         f.write(str(score))

# elif int(HiScoreStr) < score:
#     with open('HiScore.txt', 'w') as f:
#         f.write(str(score))





#Q3: Generate Multiplication tables fron 2 to 20 and write it to the different files. place these files in a folder.
# for i in range(2, 21):
#     with open(f"Tables/Multiplication_table_of_{i}", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i} x {j} = {i * j}")  

    



#Q4: A file contains a word "Donkey" multiple times. you need to write a program which replaces this word with ###### by updating the same file.
# with open("muneeb.txt") as f:
#     content = f.read()

# content = content.replace("donkey", "!@#$%^&*")

# with open("muneeb.txt", "w") as f:
#     f.write(content)







#Q5: Repeat program 4 for a list of such words to be censored.
# words = ["donkey", "kaddu", "mote"]

# with open("muneeb.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "!@#$%^&*")
#     with open("muneeb.txt", "w") as f:
#         f.write(content)






#Q6: Write a program to mine a log file and find out whether it contains 'python'.
# with open("log.txt") as f:
#     content = f.read()

# if 'Python' in content.lower():
#     print("Yes python is present")

# else:
#     print("Yes python is not present")





#Q7: Find out the line number where the python is present
content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i += 1