#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    return sum(tup[0] * tup[1] for tup in my_list) / sum(tup[1] for tup in my_list)
