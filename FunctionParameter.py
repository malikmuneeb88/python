# def addition(x, y):
#     return x + y

# # print(addition(5, 4))

# z  = addition("HEY", " THERE")

# print(z)


# def average(num1, num2):
#     return (num1 + num2)/2

# print(average(4, 3))





# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2] + marks[3])/400) * 100
#     return p

# marks1 = [34, 65, 83, 99]
# percentage1 = percent(marks1)

# marks2 = [34, 65, 83, 99]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)





# def greet(name):
# def greet(name = "Stranger"): #This is called default parameter value
#     print("Good Day " + name)

# def sum(num1, num2):
#     return num1 + num2

# greet("Muneeb")
# greet()
# s = sum(78, 9875)
# print(s)




# n = 6
# product = 1
# for i in range(n):
#     product = product * (i + 1)
# print(product)

#now we do the above program in functiuon
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product
    
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
# print(factorial_iter(3))
print(factorial_recursive(5))


