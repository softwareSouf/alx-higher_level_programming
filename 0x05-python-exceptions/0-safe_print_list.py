import random

def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(x):
        if i < len(my_list):
            print("{}".format(my_list[i]), end="")
            ret += 1
        else:
            break
    print("")
    assert ret == x, "Expected {} elements to be printed, but {} were printed".format(x, ret)
    return (ret)

if __name__ == "__main__":
    my_list = [random.randint(1, 100) for _ in range(10)]
    print(safe_print_list(my_list, 3))
