#pythagoras theorem
from math import sqrt
side1 = float(input('Enter 1st side of triangle :'))
side2 = float(input('Enter 2nd side of triangle :'))

side3 = sqrt(side1**2 + side2**2)

print('Third side of triangle is {:.4}'.format(side3))