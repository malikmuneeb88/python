print("enter your marks")

marks = int(input())
if (marks > 95 and marks< 100):
    grade = 'A++'

elif(marks > 80 and marks < 100):
    grade = 'B+'

elif(marks > 75 and marks < 100):
    grade = 'B'

elif(marks > 60 and marks < 100):
    grade = 'C'

elif(marks > 30 and marks < 100):
    grade = 'D'

elif(marks > 20 and marks < 100):
    grade = 'FAIL'

else:
    grade = 'DONT KNOWN'

print("Your grade is", grade)

