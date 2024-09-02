print("Enter your marks")

number = int(input())

if (number > 90 and number < 100):
    Grade = 'A-One'

elif (number > 80 and number < 100):
    Grade = 'A+'

elif (number > 70 and number < 100):
    Grade = 'A'

elif (number > 60 and number < 100):
    Grade = 'B'

elif (number > 50 and number < 100):
    Grade = 'C'

elif (number > 40 and number < 100):
    Grade = 'D'

elif (number > 30 and number < 100):
    Grade = 'E' 

elif (number > 20 and number < 100):
    Grade = 'Fail'

else:
    Grade = 'Dont Know' 

print("the grade is", Grade)




