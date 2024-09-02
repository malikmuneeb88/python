# Display a user entered name followed by Good Afternoon using input() function.

name = input("Enter your name:\n")
print("Good Afternoon " + name)   




# Fill in a letter template given below with name and date.

letter = '''Dear <|NAME|>,
you are selected!
Date: <|DATE|>'''

name = input("Enter your name:\n")
date = input("Enter date:\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)




#Detect Double Spaces

string = "This is a string with double  Spaces"

doubleSpaces = string.find("  ")
print(doubleSpaces)



#Replace double Space with single space

string1 = "This is a string with double  Spaces"

string1 = string1.replace("  ", " ")
print(string1)




#Escape Sequence

letter = "Dear Zain bhai, The culture you provided me is so nice! Thanks!"
print(letter)

formatted_letter = "Dear Zain bhai,\n\t The culture you provided me is so nice!\n Thanks!"
print(formatted_letter) 