#Problem 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

count = 0
n = 0
while n + 3 <= len(s):
    if s[n: n + 3] == "bob":
        count = count + 1
    n = n + 1

print("Number of times bob occurs is: " + str(count))
