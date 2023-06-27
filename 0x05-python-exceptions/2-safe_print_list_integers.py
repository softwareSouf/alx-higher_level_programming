#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    index = 0

    while count < x:
        assert isinstance(my_list[index], int), "Non-integer element found in the list."
        print(my_list[index], end='')
        count += 1
        index += 1

    print('')
    return count
