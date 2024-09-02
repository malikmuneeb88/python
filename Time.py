from time import time

def func1(a, b):
    #Zain function
    return a + b

def func2(a, b):
    #Muneeb function
    num1 = a
    num2 = b
    if(a > b and a != 3):
        pass 
    sum ([4 + 3])
    return a + b 

if __name__ == '__main__':
    init = time()
    for i in range(0, 100000000):
        func1(3, 5)
    print("Zain time", time() - init)

    init = time()
    for i in range(0, 100000000):
        func2(3, 5)
    print("Muneeb time", time() - init)



from time import time

def func1(a, b):
    #zain code
    return a + b

def func2(a, b):
    #muneeb code
    num1 = a
    num2 = b
    if (a > b and a != 3):
        pass
    sum(4 + 3)
    return a + b

if __name__ == '__main__':
    init = time()
    for i in range(0, 100000):
        func1(5, 7)
    print("zain time", time() - init)

    init = time()
    for i in range(0, 100000):
        func1(5, 7)
    print("muneeb time", time() - init)