a = {1, 2, 3, 4, 5, 3}
print(type(a))
print(a)



#Empty set
b = set()
print(type(b))



#Add items
b.add(4)
b.add(7)
b.add((5, 8, 10)) #Adding tuple 
print(b)
 

#Lenth of the set
print(len(b)) 


#Removal
b.remove(7)
print(b)

#Pop
print(b.pop())
print(b)