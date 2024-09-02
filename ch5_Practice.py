#Q1: Create a dictionary of Urdu words with values as their english translation. Provide user option to look it up.
myDict = {"Ghar": "House",
          "daftar": "Office",
          "Gali": "Street"}

print("Options are:", myDict.keys())
a = input("Enter the Urdu Word you want meaning:\n")
# print("The meaning of your word is:", myDict[a])
print("The meaning of your word is:", myDict.get(a)) #This line will not produce error



#Q2:Input eight numbers from the user and display all the unique numbers(once).
num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))
num4 = int(input("Enter number 4:\n"))
num5 = int(input("Enter number 5:\n"))
num6 = int(input("Enter number 6:\n"))
num7 = int(input("Enter number 7:\n"))
num8 = int(input("Enter number 8:\n"))
                 
s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)




#Q3: Set with same integer and same string in it.
s = {18, "18"}
print(s)




#Q4: Length of set.
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))




#Q5: What is the Type of s?
s = {}
print(type(s))




#Q6: Create an empty dictionary. Allow 4 friends to enter their favourite Languages as values and keys as their names.
favouriteLanguage = {}

a = input("Enter your Language Zain\n")
b = input("Enter your Language Abdullah\n")
c = input("Enter your Language Abubakar\n")
d = input("Enter your Language Naveed\n")

favouriteLanguage['Zain'] = a
favouriteLanguage['Abdullah'] = b
favouriteLanguage['Abubakar'] = c
favouriteLanguage['Naveed'] = d

print(favouriteLanguage)




#Q7: If names of 2 friends are same, What will happen to the program in problem 6.
favouriteLanguage = {}

a = input("Enter your Language Zain\n")
b = input("Enter your Language Abdullah\n")
c = input("Enter your Language Abubakar\n")
d = input("Enter your Language Naveed\n")

favouriteLanguage['Zain'] = a
favouriteLanguage['Abdullah'] = b
favouriteLanguage['Zain'] = c
favouriteLanguage['Naveed'] = d

print(favouriteLanguage)
