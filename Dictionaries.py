names = {'Muneeb': 22,
         'Zain': 26,
         'Abdullah': 24,
         'Kashif': 18}

print(names['Zain'])

# If i want to change zain's age  
names['Zain'] = 30
print(names['Zain'])

print(names.keys())
print(names.values())




myDict = {'Class': 'The class of fish',
          'College': 'Army Public College for boys',
          'University': 'Iqra University main Campus',
          "anotherDict": {"muneeb": "Is learning Python"}
          }

print(myDict['Class'])
print(myDict['College'])
print(myDict['University'])
print(myDict["anotherDict"]["muneeb"])

print(myDict.keys())
print(myDict.values())
print(myDict.items())
updateDict = {"Vyro": "Company",
              "Pakistan": "Country"}
myDict.update(updateDict)
print(myDict)

print(myDict.get('College'))
print(myDict['College'])