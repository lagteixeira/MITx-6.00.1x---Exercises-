import math


# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

def polysum (n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    perimeter = n * s
    sum = area + perimeter**2
    return round(sum, 4)
