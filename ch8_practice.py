#Q1: using function find the greatest of three numbers.
def maximun(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3

m = maximun(56, 73, 927)
print("The maximun value is ", str(m))



 
#Q2: Using function convert celsius to fahrenheit.
def fahrenheit(celsius):
    return (celsius * (9/5)) + 32

c = 23
f = fahrenheit(c)
print("Celsius to fahrenheit temperature is", str(f))



#Q3: How do you prevent a python print() function to print a new line at the end.
print("Hello", end=" ")
print("How", end=" ")
print("Are", end=" ")
print("You", end=" ")





#Q4: Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    
    else:
        return n + sum_of_natural_numbers(n - 1)
    
n = int(input("Enter a number :\n"))
print(f"The sum of first {n} natural numbers are : {sum_of_natural_numbers(n)}")





#Q5: Write a python function to print first n lines of the following pattern.
n = int(input("Enter a number you want :\n "))
for i in range(n):
    print("*" * (n - i))






#Q6: Write a python function which converts inches to cms.
def inches_to_cms(inches):
    conversion_factor = 2.54

    centimeters = inches * conversion_factor
    return centimeters
inches = int(input("Enter a number: \n"))
print(f"{inches} inches is equal to {inches_to_cms(inches)} centimeters")







#Q7: Write a python function to remove a given word from a string and strip it at the same time.
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "          Muneeb is a good boy       "
n = remove_and_split(this, "Muneeb")
print(n)







#Q8: print multiplication table of a given number.
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {i * number}")

number = 7
print_multiplication_table(number)