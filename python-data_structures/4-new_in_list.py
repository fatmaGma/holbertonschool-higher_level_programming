#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx >= len(my_list)):
        return (my_list)
    else:
        my_list_modif = my_list[:]
        my_list_modif[idx] = element
        return (my_list_modif)
