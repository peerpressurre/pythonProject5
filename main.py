num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))

#усі числа діапазону
print('Усі числа діапазону')
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
number1 = num1
while number1 < num2:
    print(f'number = {number1}')
    number1 += 1
else:
    print(f'number = {num1}')

print('Усі числа діапазону за спаданням')
number2 = num2
while number2 > num1:
    print(f'{number2}')
    number2 -= 1
else:
    print(f'{number2}')

print('Усі числа кратні 7')
