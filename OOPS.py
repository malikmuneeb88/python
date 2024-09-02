# class Employee:
#     name = None
#     id = 0
#     salary = 0


#     def __init__(self, name, id, salary):  
#         self.name = name
#         self.id = id
#         self.salary = salary


#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name 
    
#     def set_id(self, id):
#         self.id = id

#     def get_id(self):
#         return self.id 
    
#     def set_salary(self, salary):
#         self.salary = salary

#     def get_salary(self):
#         return self.salary
# harry = Employee('harry', 40, 2500000)
# print(harry.get_name())
# print(harry.get_id())
# print(harry.get_salary())





# #Railway Form Example:
# class RailwayForm:
#     FormType = "RailwayForm"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# harrysApplication = RailwayForm()
# harrysApplication.name = "Harry"
# harrysApplication.train = "Millat Express"
# harrysApplication.printData()




#Class attributes and instance attributes
# class Employee:
#     company = "Google"
#     salary = 100

# harry = Employee()
# muneeb = Employee()

#Creating instance attribute salary for both the objects....
# harry.salary = 500
# muneeb.salary = 600
# # muneeb.salary = 34
# print(muneeb.company)
# print(harry.company)
# Employee.company = "Youtube" #class ka name le k change krna hota hai
# print(muneeb.company)
# print(harry.company)
# print(harry.salary)
# print(muneeb.salary)









#INHERITANCE

# class Remote:
#     pass

# class Player:
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass

#     def moveTop(self):
#         pass

# remote1 = Remote()
# player1 = Player()

# if(remote1.isleftPressed()):
#     player1.moveLeft
    







#GET FUNCTION
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self):
        print(f"Salary is {self.Salary}")

    @staticmethod
    def greet():
        print("Good Morning Sir")

    @staticmethod
    def time():
        print("The time is 1AM")

harry = Employee("Muneeb", 1000, "Youtube") 
harry.getDetails()
# harry.Salary = 100000
# harry.getSalary() #Employee.getSalary(harry)  is trah bhi hum likh sktay hain
# harry.greet()     #Employee.greet()  is trah bhi hum likh sktay hain
