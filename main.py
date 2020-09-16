from tasks import task1, task2, task3, task4, task5, task6


def main():

    print('Введите номер задания:')
    n = input()
    if n == '1':
        pass
    if n == '2':
        pass
    if n == '3':
        taskcat = task3.Cat(30)
        taskcat.getBoysNumber()
        taskcat.getGirlsNumber()
    if n == '4':
        pass
    if n == '5':
        task5.numberSequence()
    if n == '6':
        lst = [1, 2, 3, 4, 5, 6]
        print(task6.modify_list(lst))  # None
        print(lst)  # [1, 2, 3]
        task6.modify_list(lst)
        print(lst)  # [1]

        lst = [10, 5, 8, 3]
        task6.modify_list(lst)
        print(lst)  # [5, 4]


if __name__ == '__main__':
    main()
