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

print(gcdIter(100, 19))
