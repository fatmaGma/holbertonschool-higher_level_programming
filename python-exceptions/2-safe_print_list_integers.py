#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
    my_list (list): The list to print elements from.
    x (int): The number of elements to access in my_list.

    Returns:
    int: The real number of integers printed.
    """
    count = 0
    printed_count = 0
    try:
        while count < x:
            try:
                print("{:d}".format(my_list[count]), end="")
                printed_count += 1
            except (ValueError, TypeError):
                pass
            count += 1
    except IndexError:
        pass
    print()  # for a new line after printing elements
    return printed_count
