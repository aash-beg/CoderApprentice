amount = 1156
dollar = amount // 100
left = amount % 100
quarters = left // 25
left = left % 25
dimes = left // 10
left = left % 10
nickels = left // 5
pennies = left % 5

print('{0} dollars, {1} qtrs, {2} dimes, {3} nickels & {4} pennies'.format(dollar, quarters, dimes, nickels, pennies))