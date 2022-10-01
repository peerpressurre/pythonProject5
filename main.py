num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))

if num1 < 7:
    num1 += (7 % num1)
elif num1 > 7:
    num1 = (num1 - (num1 % 7))+7
number = num1

while number <= num2:
    print(f'{number}')
    number += 7
