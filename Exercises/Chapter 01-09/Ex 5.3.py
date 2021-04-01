num1 = float(input('1st number: '))
num2 = float(input('2nd number: '))
num3 = float(input('3rd number: '))

large = max(num1, num2, num3)
small = min(num1, num2, num3)
avg = (num1 + num2 + num3)/3

print('Largest number is {0}\n'
      'Smallest number is {1}\n'
      'Average is {2:.2f}'.format(large, small, avg))
