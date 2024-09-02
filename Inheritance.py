# #This is SINGLE INHERITANCE code:

# #BASE CLASS
# class Employee:
#     company = "Google"

#     def showDetails(self):
#         print("This is an employee")

# #DERIVED CLASS OR CHILD CLASS
# class Programmer(Employee):
#     language = "Python"
#     company = "YouTube"

#     def getLanguage(self):
#         print(f"The language is {self.language}")

#     def showDetails(self):
#         print("This is a programmer")

# e = Employee()
# e.showDetails()
# p = Programmer()
# p.showDetails() 
# print(p.company)




# #This is MULTIPLE INHERITANCE Code :
# class Employee:
#     company = "Visa"
#     eCode = 135

# class Freelancer:
#     company = "Fiverr"
#     level = 0

#     def upgardeLevel(self):
#         self.level = self.level + 1

# class Programmer(Employee, Freelancer):
#     name = "Muneeb"
    
# p = Programmer()
# p.upgardeLevel()
# print(p.level)
# print(p.company)






# #This is MULTILEVEL INHERITANCE Code :
# class Person:
#     country = "India"

#     def takeBreath(self):
#         print("I am breathing")

# class Employee(Person):
#     company = "Honda"

#     def getSalaray(self):
#         print(f"Salary is {self.salaray}")

#     def takeBreath(self):
#         print("I am not Breathing")

# class Programmer(Employee):
#     company = "Fiverr"

#     def getSalaray(self):
#         print(f"No Salary for Programmer")

#     def takeBreath(self):
#         print("I am  Breathing ++")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()
# print(e.company)

# pr = Programmer()
# pr.takeBreath()  
# print(pr.company)





# #CLASS METHOD:
# class Employee:
#     company = "DELL"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.__class__.salary = sal

#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(5500)
# print(e.salary)








#OPERATOR OVERLOADING METHOD:
# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print("Lets add")
#         return self.num + num2.num
    
#     def __mul__(self, num2):
#         print("Lets Multiply")
#         return self.num * num2.num
    
# n1 = Number(34)
# n2 = Number(45)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)






#OTHER DUNDER METHODS;
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1

n = Number(9)
print(n)
print(len(n))