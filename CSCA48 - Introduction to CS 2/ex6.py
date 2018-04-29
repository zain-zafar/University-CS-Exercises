def rsum(any_list, holder = 0):
    '''(List of int) -> int
    REQ: length of list is greater than 0, len(any_list) > 0
    >>> rsum([1,2,3])
    6
    >>> rsum([[3],4,5])
    12
    >>> rsum([[1]])
    1
    Returns the sum of all int elements in the list
    '''
    # the base case, where each element is added to a new list, then list is
    # returned.
    if isinstance(any_list[0], int) and len(any_list) == 1:
        holder += any_list[0]
        return holder

    else:
        # if list is int, recurse by adding each element into a list one at a
        # time
        if (isinstance(any_list[0], int) and len(any_list) > 1):
            # Add each first element into a list
            holder += any_list[0]
            # Recurse on the remaining list
            return rsum(any_list[1:], holder)

        # if the list has more than 1 element, and has empty first element
        elif (len(any_list) > 1 and any_list[0] == []):
            # recurse the list by removing that element
            return rsum(any_list[1:], holder)

        # if the list contains list which isnt empty, run rsum on the list
        elif isinstance(any_list[0], list) and any_list[0] != []:
            return rsum(any_list[0] + any_list[1:], holder)
        # if the first element is 0, then perform rsum on the list
        else:
            any_list[0] = 0
            return rsum(any_list, holder)



def rmax(any_list, largest_val=float('-inf')):
    '''(List of int) -> int
    REQ: any_list has length greater than 0

    >>> any_list = [1,2,3,3,4,5,6,5,3,2]
    rmax(any_list)
    6
    >>> any_list = [1]
    rmax(any_list)
    1
    Return the greatest integer value in the list of int.
    '''
    any_list = flatten_list(any_list)
    # Check and see if the first element in list is smaller than - infinity.
    # Since, this will always be true, largest_val can be initialized
    if largest_val < any_list[0]:
        largest_val = any_list[0]

    # Base case, where list contains only 1 element, return largest_val.
    # Base case values is the first element in the list.
    if len(any_list) == 1:
        return largest_val
    # recursive step, where list contains more than 1 element
    else:
        # Return the list after the first element, and recurse, to compare each
        # first element in the list and see if it is greater than the next.
        return rmax(any_list[1:], largest_val)



def second_smallest(any_list, min_val_2=float('+inf'), min_val=float('+inf')):
    '''(List of int) -> int
    REQ: any_list has length greater than 0, len(any_list) > 0

    >>> any_list = [1,2,3,3,4,5,6,5,3,2]
    second_smallest(any_list)
    2

    >>> any_list = [1,1,2]
    second_smallest(any_list)
    1

    >>> any_list = [1,1]
    second_smallest(any_list)
    1

    Return the greatest integer value in the list of int.
    '''
    any_list = flatten_list(any_list)
    # find the minimum value in the list, by setting it equal to the
    # first element value
    if min_val > any_list[0]:
        min_val = any_list[0]

    # Find the second lowest value, by checking if the lowest value in the list
    # is greater than or equal to the first element in the list and also if
    # first element in list is less than or equal to min_value2, then the
    # second lowest value will become the first element of the list
    if any_list[1] >= min_val and any_list[1] <= min_val_2:
        min_val_2 = any_list[1]

    # The base case is 2, this is where second minimum value can be found
    if len(any_list) == 2:
        return min_val_2

    else:
        # use recursion, to call the function and cycle through all
        # first elements of the list, to check and find the second
        # smallest value
        return second_smallest(any_list[1:], min_val_2, min_val)



def sum_max_min(any_list, max_value=float('-inf'), min_value=float('+inf')):
    '''(List of int) -> int
    REQ: len(any_list) > 0

    >>> any_list = [1,1,1,[1,1,1],[2]]
    sum_max_min(any_list)
    3

    >>> any_list = [2]
    sum_max_min(any_list)
    4

    Returns the sum of the largest and smallest integer value in the list.
    '''
    any_list = flatten_list(any_list)
    # check if max_value is smaller than first element in list:
    if max_value < any_list[0]:
        # if true, then store the first element as max_value
        max_value = any_list[0]

    # check if min_value is greater than the first element in list:
    if min_value > any_list[0]:
        min_value = any_list[0]

    # Base case, where length of list is 1, and this returns the sum of
    # min and max values
    if len(any_list) == 1:
        return (min_value + max_value)

    else:
        # Recursive step, where the function is called upon, with the same
        # list, with its first element removed, this way, there can be a
        # new max and min value, and the list is only cycled once.
        return sum_max_min(any_list[1:], max_value, min_value)



def flatten_list(any_list):
    ''' (list) -> list
    This function will take a nested list and flatten it out into a single
    list
    >>>flatten_list([[1,2,3],[7],[[9,87,-1]]])
    [9, 87, -1, 1, 2, 3, 7]
    >>>flatten_list([[[[[]]]]])
    []
    >>>flatten_list([100,99,98])
    [100, 99, 98]
    '''
    # Call the helper function to check whether the list is nested is not
    lister = multiple_lists(any_list)
    # If its not nested then return the original list
    if(lister):
        return any_list
    # Otherwise we have a nested list
    else:
        # If list of list is found then recursively call the same function on
        # the rest of the list and removing the first element and adding it in
        # the base level at the beginning
        if(isinstance(any_list[0], list) and any_list[0] != []):
            return flatten_list(any_list[0] + any_list[1:])
        # If list of integers is found then recursively call the small function
        # on the rest of the list and removing the first element and adding
        # it in the end at the base level
        elif(isinstance(any_list[0], int) and len(any_list) > 1):
            return flatten_list(any_list[1:] + [any_list[0]])
        # If list of empty list is found then just recurse on the rest of the
        # list
        elif(any_list[0] == [] and len(any_list) > 1):
            return flatten_list(any_list[1:])
        # If an empty list is found then we don't require that so delete it
        elif(any_list[0] == []):
            del any_list[0]
            return flatten_list(any_list)


def multiple_lists(any_list):
    '''(list) -> bool
    This function will check whether the list is nested or not. It will return
    True if and only if the list is not nested
    >>>multiple_lists([1,2,3,[4]])
    False
    >>>multiple_lists([1,2,3])
    True
    '''
    # Loop through each element in the given list
    for elements in any_list:
        # Check to see if the type is a list and return False if nested list
        # is found
        if(isinstance(elements, list)):
            return False
    # Otherwise return True
    return True
