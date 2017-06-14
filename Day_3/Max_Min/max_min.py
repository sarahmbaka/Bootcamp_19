def find_max_min(user_list):
    """    
    Function that returns the maximum and minimum values in a list

    """

    # checks the list and compares the values
    if len(set(user_list)) > 1:
        return [min(user_list), max(user_list)]
    else:
        return [user_list[0]]


print(find_max_min([1, 2, 3, 4]))

print(find_max_min([4, 4, 4, 4]))
