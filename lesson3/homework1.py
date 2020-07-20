# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def devide():
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    if a == 0:
        print("Can't devide by 0")
    elif b == 0:
        print("Can't devide by 0")
    else:
        result = a / b
    print(round(result,2))

devide()

