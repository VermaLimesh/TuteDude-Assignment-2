#Task 1: Check if a Number is Even or Odd


a = int(input('Enter a number: '))       # Takes an integer input from the user.

if (a % 2) == 0:                         # Checks whether the number is even or odd
    print(f'{a} is an Even Number.')
else:
    print(f'{a} is an Odd Number.')
