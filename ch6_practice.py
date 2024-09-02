#Q1: Write a program to find greatest of four numbers entered by the user.
# (num1 = int(input("Enter number 1:\n"))
# num2 = int(input("Enter number 2:\n"))
# num3 = int(input("Enter number 3:\n"))
# num4 = int(input("Enter number 4:\n"))

# if(num1 > num4):
#     f1 = num1

# else:
#     f1 = num4

# if(num2 > num3):
#     f2 = num2
# else:
#     f2 = num4

# if(f1 > f2):
#     print(str(f1) + " is greater")

# else:
#     print(str(f2) + " is greater"))




# Q2: Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33%
# in each subject to pass. Assume 3 subjects and take marks as an input from the user
# subject1 = int(input("Enter first subject marks : "))
# subject2 = int(input("Enter second subject marks :"))
# subject3 = int(input("Enter third subject marks : "))

# if(subject1 < 33 or subject2 < 33 or subject3 < 33):
#     print("You are fail due to less than 33 marks in one of the subjects")

# elif(subject1 + subject2 + subject3)/3 < 40:
#     print("You are fail because you have less than 40 percentage")

# else:
#     print("Congratulations! Your are passed")




#Q3: A spam comment is defined as a text containing following keywords:
# Text = input("Enter the Text :\n")

# if("make a lot of money" in Text):
#     spam = True

# elif("buy now" in Text):
#     spam = True

# elif("subscribe this" in Text):
#     spam = True

# elif("click this" in Text):
#     spam = True

# else:
#     spam = False


# if(spam):
#     print("This text is spam")

# else:
#     print("This text is not spam")




#Q4: Find whether a given username contains less than 10 characters or not.
# username = input("Enter username :")

# if len (username) < 10:
#     print("the username has less than 10 characters")

# elif len (username) > 10:
#     print("The username has more than 10 characters")

# else:
#     print("The username has 10 characters")




#Q5: find out whether a given name is present in a list or not.
# names = ["Zain", "Abdullah", "Kashif", "Muneeb"]
# name = input("Enter name to check\n")

# if name in names:
#     print("Your name is present in list")

# else:
#     print("Your name is not present in list")




#Q6: Calculate grade of a student.
# marks = int(input("Enter your Marks :\n"))

# if(marks >= 90):
#     grade = "A-One"

# elif(marks >= 80):
#     grade = "A"

# elif(marks >= 70):
#     grade = "B"

# elif(marks >= 60):
#     grade = "C"

# elif(marks >= 50):
#     grade = "D"

# else:
#     grade = "F"

# print("Your Grade is " + grade)




#Q7: find out whether a given post is talking about "Harry" or not.
names = ['HARRY', 'HaRrY', 'harry', 'haRRy', 'Harry']
post = input("Enter the post\n")

if post in names:
    print("The post is talking about Harry.")

else:
    print("The post is not talking about Haryr.")

