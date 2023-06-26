#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0

    while count < x and index < len(my_list):
        if isinstance(my_list[index], int):
            print(my_list[index], end='')
            count += 1
        index += 1

    print('')
    return count
