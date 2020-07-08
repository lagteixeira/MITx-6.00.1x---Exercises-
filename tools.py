import math

def square(x):
    '''
    x: int or float.
    '''
    return x * x

def recurPower (base, exp):
    if exp == 0:
        return 1
    return base * recurPower(base, exp - 1)

def gcdIter(a, b):
    if a >= b:
        testvalue = b
    else: testvalue = a
    while not(a%testvalue == 0 and b%testvalue == 0):
        testvalue -= 1
    return testvalue

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''


    if b == 0:
        return a
    return gcdRecur(b, a%b)

def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[(len(aStr) // 2)]:
        return True
    elif char > aStr[(len(aStr) // 2)]:
        isIn(char,aStr[len(aStr) // 2 + 1 :])
    else:
        isIn(char, aStr[: len(aStr) // 2 - 1])


print (isIn("a", "agkw"))

string = "agkw"

print (string [len(string)//2])
print(string [: len(string)// 2 - 1])

print ("a" > "k")
