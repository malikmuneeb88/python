#Store seven fruits in a list entered by the user.

L1 = input("Enter fruit numberb 1: ")
L2 = input("Enter fruit numberb 2: ")
L3 = input("Enter fruit numberb 3: ")
L4 = input("Enter fruit numberb 4: ")
L5 = input("Enter fruit numberb 5: ")
L6 = input("Enter fruit numberb 6: ")
L7 = input("Enter fruit numberb 7: ")

myFruitsList = [L1, L2, L3, L4, L5, L6, L7]
print(myFruitsList)



#Accept marks of 6 students and display them in a sorted manner.

S1 = input("Enter marks of student 1: ")
S2 = input("Enter marks of student 2: ")
S3 = input("Enter marks of student 3: ")
S4 = input("Enter marks of student 4: ")
S5 = input("Enter marks of student 5: ")
S6 = input("Enter marks of student 6: ")
S7 = input("Enter marks of student 7: ")

marksOfStudents = [S1, S2, S3, S4, S5, S6, S7]
print(marksOfStudents)

marksOfStudents.sort()
print(marksOfStudents)




# #Sum a list with 4 numbers

a = [3, 56, 7, 90]
print(a[0] + a[1] + a[2] + a[3])
# print(sum(a))



# Count the number of zeroes in the following tuple.

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))