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
        task5.numberSequence(7)
    if n == '6':
        pass


if __name__ == '__main__':
    main()
