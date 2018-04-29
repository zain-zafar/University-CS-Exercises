def rsum(any_list):
    '''(list of int) -> int
    REQ: Length of the list must be greater than 0
    This function will add up all the integers in the given list of integers
    >>>rsum([9,1000,-1000,57,78,0])
    144
    >>>rsum([1])
    1
    '''
    # Base case for one element
    if len(any_list) == 1:
        # Return that integer
        return any_list[0]
    # Otherwise keep breaking the list and adding the previous number
    else:
        return any_list[0] + rsum(any_list[1:])

def rmax(any_list):
    '''(list of int) -> int
    REQ: Length of the list must be greater than 0
    This function will find the greatest integer in the given list
    >>>rmax([9,1000,-1000,57,78,0])
    1000
    >>>rmax([180])
    180
    '''
    # Base case for one element
    if len(any_list) == 1:
        # That is the maximum integer
        return any_list[0]
    # Otherwise keep breaking the list using same function
    else:
        result = rmax(any_list[1:])
        # If the result is greater then return it
        if result > any_list[0]:
            return result
        # Else return the previous integer
        else:
            return any_list[0]

def second_smallest(L):
    '''(list of int) -> int
    REQ: Length of the list must be greater than 1
    This function will find the second smallest integer in the given list
    >>>second_smallest([[9,1000],[0],[],[[1,2,3],-1000]])
    0
    >>>second_smallest([[1],[[1,1],[1]]])
    1
    >>>second_smallest([[],[[2],9,8,8]])
    8
    '''
    # Get the tuple contaning smallest and second smallest integers
    result = helper_second_min(L)
    # Return the second smallest integer
    return result[1]


def sum_max_min(L):
    '''(list of int) -> int
    REQ: Length of the list must be greater than 0
    This function will add the lowest and highest integers and output the sum
    in the given list
    >>>sum_max_min([[9,1000],[0],[],[[1,2,3],-1000]])
    0
    >>>sum_max_min([[1],[[1,1],[1]]])
    2
    >>>sum_max_min([[[[[10]]]]])
    20
    '''
    # Get the tuple containing the smallest and the largest integers
    result = helper_max_min(L)
    # Return the sum of those integers
    return result[0] + result[1]

# Helper Functions


def helper_second_min(L):
    ''' (list) -> tuple
    REQ: Length of the list must be greater than 1
    This function will take any given list and it will return the smallest and
    the second smallest integers in the list
    '''
    # Base Case: If there are only two integers to compare
    if len(L) == 2:
        # Then the larger integer is second smallest and the other is the
        # smallest
        if L[0] < L[1]:
            smallest = L[0]
            ssmallest = L[1]
            return (smallest, ssmallest)
        else:
            smallest = L[1]
            ssmallest = L[0]
            return (smallest, ssmallest)
    # Else recursivley call the function again until it has len(L) == 2
    else:
        result = helper_second_min(L[1:])
        # If the smallest number in tuple is greater than the next integer
        if result[0] > L[0]:
            # If the second smallest integer in the tuple is greater
            if result[1] > L[0]:
                # Then update the smallest integer
                (smallest, ssmallest) = (L[0], result[0])
            # Otherwise update the second smallest integer
            else:
                (smallest, ssmallest) = (L[0], result[1])
        # If the second smallest number in tuple is greater than the next
        # integer
        elif result[1] > L[0]:
            # If the smallest integer is greater than the next integer
            if result[0] > L[0]:
                # Then update the second smallest integer
                (smallest, ssmallest) = (result[1], L[0])
            # Otherwise update the smallest integer
            else:
                (smallest, ssmallest) = (result[0], L[0])
        # If the integer found is greater than both our integers in the tuple
        # then move on to the next integer in the list and do not update
        else:
            (smallest, ssmallest) = (result[0], result[1])
    # Return the tuple of the smallest and the second smallest integers
    return (smallest, ssmallest)


def helper_max_min(L):
    '''(list) -> tuple
    REQ: Length of the list must be greater than 0
    This function will take in any given list and return the tuple of the
    maximum and the minimum integers
    '''
    # Base Case: If there is only one integer in the list
    if len(L) == 1:
        # Then the integer is the max and the min of the list
        maximum = minimum = L[0]
        return (maximum, minimum)
    # Else recursively call the function again
    else:
        result = helper_max_min(L[1:])
        # If the maximum integer is greater than the next integer than don't
        # update
        if result[0] > L[0]:
            (maximum, minimum) = (result[0], result[1])
        # Otherwise update the maximum integer
        else:
            (maximum, minimum) = (L[0], result[1])
        # If the minimum integer is lower then the next integer than don't
        # update
        if result[1] < L[0]:
            (maximum, minimum) = (maximum, result[1])
        # Otherwise don't update the minimum integer
        else:
            (maximum, minimum) = (maximum, L[0])
    # Return the tuple of the maximum and the minimum integers
    return (maximum, minimum)

# HOW TO SIMPLIFY ANY TYPE OF LIST OF INTEGERS

def flatten_list(L):
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
    single_list = multiple_lists(L)
    # If its not nested then return the original list
    if(single_list):
        return L
    # Otherwise we have a nested list
    else:
        # If list of list is found then recursively call the same function on
        # the rest of the list and removing the first element and adding it in
        # the base level at the beginning
        if(isinstance(L[0], list) and L[0] != []):
            return flatten_list(L[0] + L[1:])
        # If list of integers is found then recursively call the small function
        # on the rest of the list and removing the first element and adding
        # it in the end at the base level
        elif(isinstance(L[0], int) and len(L) > 1):
            return flatten_list(L[1:] + [L[0]])
        # If list of empty list is found then just recurse on the rest of the
        # list
        elif(L[0] == [] and len(L) > 1):
            return flatten_list(L[1:])
        # If an empty list is found then we don't require that so delete it
        elif(L[0] == []):
            del L[0]
            return flatten_list(L)


def multiple_lists(L):
    '''(list) -> bool
    This function will check whether the list is nested or not. It will return
    True if and only if the list is not nested
    >>>multiple_lists([1,2,3,[4]])
    False
    >>>multiple_lists([1,2,3])
    True
    '''
    # Loop through each element in the given list
    for elements in L:
        # Check to see if the type is a list and return False if nested list
        # is found
        if(isinstance(elements, list)):
            return False
    # Otherwise return True
    return True