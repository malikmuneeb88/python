# file = open("muneeb.txt", "wb")
# print(file.mode)

# print(file.name)

# file.write(bytes("write this to my file", "UTF-8"))

# file.close()

# Reading the content of a file

# file = open ('muneeb.txt', 'r+')
# text_to_read = file.read()
# print(text_to_read)

# file = open('muneeb.txt', 'r' )
# # data = file.read()
# data = file.readline( )
# print(data)
# file.close()

file = open('harry.txt', 'w')
file.write("Please2 write this to my new file which i created with the help of code")
#Jitni dfa write kren gay utni dfa file mn addd hota rhay ga
file.write("Please2 write this to my new file which i created with the help of code")
file.write("Please2 write this to my new file which i created with the help of code")
file.write("Please2 write this to my new file which i created with the help of code")
file.close()

# file = open('harry.txt', 'a')
# file.write("I am appending")
# file.close()  



#With function se hamen file close krne ki zrurat nhi hoti, automatically close hojati hai.
# with open('harry.txt', 'r') as f:
#     a = f.read()
# print(a)

# with open('harry.txt', 'w') as f:
#     a = f.write("me")
# print(a) 