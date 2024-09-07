def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def calculator():
   # print("Enter E for exit")
   
   while exit!='E':
      print("Welcome to Calculator:\n")
      num1 = float(input("Enter First Number:\n"))
   
      operation = input("Enter operations: (+), (-), (*), or (/) ")
      num2 = float(input("Enter Second Number:\n"))
      exit=input("Press E for exit")
      
      if operation == "exit":
         break
         
      if operation == "+":
         result =  add(num1, num2)
      
      elif operation == "-":
         result =  subtract(num1, num2)
      
      elif operation == "*":
         result =  multiply(num1, num2)
      
      elif operation == "/":
         result =  divide(num1, num2)
      
      else:
         print("Invalid Operation !")
         
      print(f"Your result is {result}\n")
      
      
      
calculator()