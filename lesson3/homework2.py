# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.



def info():
    dict_template = {
        'name': ('Enter your name\n', str),
        'family_name': ('Enter your family name\n', str),
        'birth_year': ('Enter your birth year\n', int),
        'city': ('Enter your city\n', str),
        'email': ('Enter your email\n', str),
        'phone': ('Enter your phone number\n', int)
    }
    info_dict = {}
    for key, value in dict_template.items():
        while True:
            user_value = input(value[0])
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nWrong answer')
                continue
            info_dict[key] = user_value
            break
    print(info_dict)

info()



