"""
Задание 2
Есть строка, содержащая текст и целые числа. Напишите функцию, которая создаёт список из целых чисел в строке.
"""


def digits():
    """

    :return:
    """
    result = ''
    print('Введите строку: ')
    s = input()
    for i in range(len(s)):
        sp = list(s)
        if sp[i].isdigit():
            result += sp[i] + ' '
        else:
            pass
    print(result)
