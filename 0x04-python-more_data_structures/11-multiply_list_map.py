#!/usr/bin/python3
def multiply_list_map(my_list=[], number=1):
    if not my_list:
        return []
    return [i * number for i in my_list]
