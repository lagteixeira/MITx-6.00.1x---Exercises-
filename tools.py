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
    return gcd(b, a%b)
