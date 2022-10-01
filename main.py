num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))

#усі числа діапазону
print('Усі числа діапазону')
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
while num1 < num2:
    print(f'number = {num1}')
    num1 += 1
else:
    print(f'number = {num1}')

print('Усі числа діапазону за спаданням')
while num2 > num1:
    print(f'{num2}')
    num2-= 1
else:
    print(f'{num2}')