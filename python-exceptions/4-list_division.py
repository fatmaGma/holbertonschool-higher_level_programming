#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
    my_list_1 (list): The first list of elements.
    my_list_2 (list): The second list of elements.
    list_length (int): The number of elements to divide.

    Returns:
    list: A new list of length list_length with the division results.
    """
    result_list = []
    for i in range(list_length):
        try:
            try:
                num1 = my_list_1[i]
            except IndexError:
                print("out of range")
                num1 = 0
            try:
                num2 = my_list_2[i]
            except IndexError:
                print("out of range")
                num2 = 1  # set to 1 to avoid division by zero
            try:
                result = num1 / num2
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
        finally:
            result_list.append(result)
    return (result_list)
