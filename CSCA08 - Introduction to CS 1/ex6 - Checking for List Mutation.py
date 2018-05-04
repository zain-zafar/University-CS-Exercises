def copy_me(input_list):
    ''' (list) -> (list)
    REQ: input_list is not to be mutated, left unchanged
    REQ: len of input_list > 0
    >>> copy_me(['abc', 123, True])
    ['ABC', 124, False]
    >>> copy_me([1, 2, 3, 4, 5, 'agt', 11.2, False])
    [2, 3, 4, 5, 6, 'AGT', '12.2', True]
    >>> copy_me([True, ['2344'], False, 123, 'abcd', 123.2])
    [False, 'List', True, 124, 'ABCD', 124.2]
    Return a list which clones the input list with a few exceptions, where
    strings are all turned to upper, int and float have values increased
    by 1, booleans are flipped (True will become false) and List inside of the
    input list are replaced by 'List'
    '''
    count = 0
    # Clone the given string, to aviod mutation.
    remake = input_list[:]
    # Check all the elements in the list, to find out their data types.
    while(count < len(remake)):
        # If the element at index is a str, then make it capital
        if (type(remake[count]) == str):
            remake[count] = remake[count].upper()
        # If the element at index is int, add 1 to it
        elif (type(remake[count]) == int):
            remake[count] = remake[count] + 1
        # If element at index is type float, then add 1 to it
        elif (type(remake[count]) == float):
            remake[count] = remake[count] + 1
        # If element at index is boolean, then reverse it. True will
        # become False, False will become True.
        elif (type(remake[count]) == bool):
            remake[count] = not remake[count]
        # If element at index is a list, then replace it with "List"
        elif (type(remake[count]) == list):
            remake[count] = "List"
        # Adding a counter allows to check every element in the given list.
        count += 1
    return remake


def mutate_me(input_list):
    ''' (list) -> (list)
    REQ: len of input_list > 0
    >>> mutate_me(['abc', 123, True])
    >>> mutate_me([1, 2, 3, 4, 5, 'agt', 11.2, False])
    >>> mutate_me([True, ['2344'], False, 123, 'abcd', 123.2])
    These values can be tested in the python shell by first initializing
    input_list, such as:
    input_list = [True, ['2344'], False, 123, 'abcd', 123.2]
    then by running the variable in the function:
    mutate_me(input_list)
    and then checking if the value of the input_list is the same after and
    before the program ran:
    input_list == ['abc', 123, True]
    input_list == [1, 2, 3, 4, 5, 'agt', 11.2, False]
    input_list == [True, ['2344'], False, 123, 'abcd', 123.2]
    all the retured values are False, which means that input_list was
    changed, mutated.
    Return a list which mutates the input list with a few exceptions, where
    strings are all turned to upper, int and float have values increased
    by 1, booleans are flipped (True will become false) and List inside of the
    input list are replaced by 'List'. The same list is overwritten, therefore
    mutated.
    '''
    count = 0
    # Check all the elements in the list, to find out their data types.
    while(count < len(input_list)):
        # If the element at index is a str, then make it capital
        if (type(input_list[count]) == str):
            input_list[count] = input_list[count].upper()
        # If the element at index is int, add 1 to it
        elif (type(input_list[count]) == int):
            input_list[count] = input_list[count] + 1
        # If element at index is type float, then add 1 to it
        elif (type(input_list[count]) == float):
            input_list[count] = input_list[count] + 1
        # If element at index is boolean, then reverse it. True will
        # become False, False will become True.
        elif (type(input_list[count]) == bool):
            input_list[count] = not input_list[count]
        # If element at index is a list, then replace it with "List"
        elif (type(input_list[count]) == list):
            input_list[count] = "List"
        # Adding a counter allows to check every element in the given list.
        count += 1
