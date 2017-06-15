def find_missing(list1, list2):
    """Function that returns the difference between two lists"""
    if not list1 and list2: # checks if list is empty
        return 0

    diff = list(set(list1) ^ set(list2)) # diff is the difference between the lists

    if not diff:
        return 0
    return diff[0] #retrieve first item in the list
