num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))
#усі числа діапазону
while num1 < num2:
    print(f'number = {num1}')
    num1 += 1
else:
    print(f'number = {num1})
#в порядку спадання
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

while num2 > num1:
    print(f'{num2}')
    num2 -= 1
else:
    print(f'{num2}')
#кратне 7
if num1 < 7:
    num1 += (7 % num1)
elif num1 > 7:
    num1 = (num1 - (num1 % 7))+7
number = num1

while number <= num2:
    print(f'{number}')
    number += 7
#кратне 5
if num1 < 5:
    num1 += (5 % num1)
elif num1 > 5:
    num1 = (num1 - (num1 % 5))+5
number = num1

while number <= num2:
    print(f'{number}')
    number += 5

