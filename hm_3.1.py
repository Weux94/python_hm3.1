digit_1 = int(input('Enter first number '))
digit_2 = int(input('Enter second number '))
sign = input('chose you sign: ')

if sign == '+':
    print(digit_1 + digit_2)
elif sign == '-':
    print(digit_1 - digit_2)
elif sign == '/':
    if digit_2 != 0:
        num_1 = float(digit_1 / digit_2).__round__(2)
        print(num_1)
    else:
        print('impossible to devide by zero')
elif sign == '*':
    print(digit_1 * digit_2)
else:
    print('wrong instruction')
