#Q1: Print Multiplication table of a given number.(FOR LOOP)
num = int(input("Enter the number :\n"))

for i in range(1, 11):
    # print(str(num) + " x " + str(i) + " = " + str(i * num))
    print(f"{num} x {i} = {num * i}")




#Q2: Write a program to greet all the person names stored in a list l1 and which starts with S.
L1 = ["Muneeb", "Syed", "Zain", "Shah"]
for name in L1:
   if name.startswith("S"):
       print("Assalam u alaikum " + name)





#Q3: Attempt problem 1 using While Loop.
num = int(input("Enter a number :\n"))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i = i + 1




#Q4: FInd out whether a given number is prime or not.
num = int(input("Enter a number :  \n"))

prime = True

for i in range(2, num):
    if(num % i == 0):
        prime = False
        break

if prime:
    print("The number is prime")

else:
    print("The number is not prime")





#Q5: Find the sum of first n natural numbers using While Loop.
def sum_of_natural_numbers(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

# Example usage:
n = 10  # You can change this value to any positive integer
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers(n)}")



#Q6: Calculate the factorial of a given number
num = int(input("Enter a number :\n"))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")






#Q7: Print the following star pattern.
n = 3
for i in range(3):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print(" " * (n - i - 1))




#Q8: Print the following star pattern.
n = 4
for i in range(4):
    print("*" * (i + 1))






#Q9: Print multiplication table in a reverse order.
num = int(input("Enter a number :\n"))

for i in reversed(range(1, 11)):
    print(f"{num} x {i} = {num * i}")