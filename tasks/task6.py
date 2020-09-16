def modify_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            lst[i] //= 2
        else:
            lst.pop(i)


