#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    """Prints the first x elements of a list snd only ints.
    Args:
        my_list (list): The list elements are printed from.
        x (int): The num of elements of my_list to print.
    Returns:
        The num of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
