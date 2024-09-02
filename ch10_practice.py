#Q1: Create a class programmer for storing information of few programmers woking at microsoft .
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

Muneeb = Programmer("Muneeb", "Skype")
Ahmed = Programmer("Ahmed", "Twitter")
Muneeb.getInfo()
Ahmed.getInfo()




#Q2: Write a class calculator capable if finding square, cube and squareroot of a number .
class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num ** 3}")

    def squareRoot(self):
        print(f"The value of {self.num} square root is {self.num ** 0.5}")

a = Calculator(9)
a.square()
a.cube()
a.squareRoot()







#Q3: Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. Does this change the class attribute ?
class Sample:
    a = "Muneeb"

object = Sample()
object.a = "Ahmed"
print(Sample.a)
print(object.a)
# Sample.a = "Zain"   #Is se change hota hai






#Q4: Add a static method in problem 2 to greet the user with hello . 
class Calculator:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def greet():
        print("Hello")

    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num ** 3}")

    def squareRoot(self):
        print(f"The value of {self.num} square root is {self.num ** 0.5}")

a = Calculator(9)
a.square()
a.cube()
a.squareRoot()
a.greet() 







#Q5: Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of trains running under Pkaistani trains . 
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is {self.fare}")
        print(f"The seats availabe in the train are {self.seats}")

    def bookTickets(self):
        if(self.seats):
            print(f"Your ticket has been booked! Your seat no. is {self.seats}")
        else:
            print("The train is Full !")

intercity = Train("Millat Express", 100, 5)
intercity.getStatus()
intercity.bookTickets()