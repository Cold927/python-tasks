def numberSequence(n):
    print('Введите число: ')
    list, amount_repeat = [], int(input())
    for i in range(amount_repeat):
        repeat = 0
        while repeat < i:
            list.append(i)
            repeat += 1
            if len(list) == amount_repeat:
                print(*list)
                break
    if amount_repeat == 1:
        print(amount_repeat)
