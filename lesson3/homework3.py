# 3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func():                      #используя функцию sorted
    numbers = []
    i = 0
    while i != 3:
        numbers.append(int(input("Enter a number: ")))
        i+=1

    numbers = sorted(numbers, reverse=True)
    print(numbers[:2])

my_func()



def second_func():                      #не используя функцию sorted
    s_numbers = []
    i = 0
    while i != 3:
        s_numbers.append(int(input("Enter a number: ")))
        i += 1
    print(s_numbers)
    t_numbers = []
    i = 0
    while i!=3:
        t_numbers.append(max(s_numbers))
        s_numbers.remove(max(s_numbers))
        i += 1
    print(t_numbers)
    print(t_numbers[:2])

second_func()