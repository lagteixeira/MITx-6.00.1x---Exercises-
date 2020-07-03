# Problem 3

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

# alphabet: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

## first, we need to build our library, association the letters of the alphabet to an order of integers.
d = {"":-1, "a": 0, "b" :1, "c" :2, "d" :3, "e" :4, "f" :5,
"g" :6, "h" :7, "i" :8, "j" :9, "k" :10, "l" :11,
"m" :12, "n" :13, "o" :14, "p" :15, "q" :16, "r" :17,
"s" :18, "t" :19, "u" :20, "v" :21, "w" :22, "x" :23, "y" :24, "z" :25}

## we will be using three auxiliary functions:
## laststring keeps track of the string - which needs to have letters in alphabetical order - we are building right now.
## lastletter keeps track of the previous letter inserted into our laststring.
## LongestStringSoFar has an obvious task.

lastletter = ""
laststring = ""
LongestStringSoFar = ""
s = 'abcdefghijklmnopqrstuvwxyz'

for letter in s:
    if d[letter] >= d[lastletter]:
        laststring = laststring + letter
        lastletter = letter
    else:
        if len(laststring) > len(LongestStringSoFar):
            LongestStringSoFar = laststring
        laststring = letter
        lastletter = letter
if len(laststring) > len(LongestStringSoFar):
    LongestStringSoFar = laststring

print ("Longest substring in alphabetical order is: " + LongestStringSoFar)
