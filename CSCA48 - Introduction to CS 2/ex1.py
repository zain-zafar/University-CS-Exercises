def greeting(name_of_person):
    '''(str) -> str
    REQ: parameter should be expected to be name of person

    >>> greeting('Zain')
    'Hello Zain how are you today?'

    Returns a message which uses the given parameter.
    '''
    return 'Hello ' + name_of_person + ' how are you today?'


def mutate_list(list_to_mute):
    '''(list) -> NoneType
    REQ: First paramter must be a list
    REQ: List must have atleast 1 element
    REQ: Str elements in the list must have atleast 2 characters

    >>> a = [1,2,3,True,False,'yes']
    >>> b = mutate_list(a)
    >>> b == a
    False
    # this shows the elements inside the list have changed

    >>> a = [1,2,3]
    >>> b = mutate_list(a)
    >>> b is a
    False
    # this shows the elements were changed, which changed object location,
    this means that the lists are not the same as one has been changed.

    Return the mutated version of the list. If the given list contains str,
    it has its first and last letters removed. If list contains bool, it is
    flipped. If list contains int, the value is doubled. The final list also
    has its first element changed to 'Hello'.
    '''
    counter = 0
    while counter < len(list_to_mute):
        # check if list contains string
        if type(list_to_mute[counter]) == str:
            # If it does, remove first letter from it
            list_to_mute[counter] = list_to_mute[counter][1:]
            # Find the last index from those strings
            last_letter = len(list_to_mute[counter]) - 1
            # Now remove the last letter from the string
            list_to_mute[counter] = list_to_mute[counter][:last_letter]

        # check if list contains int
        if type(list_to_mute[counter]) == int:
            # Multiply each value by 2
            list_to_mute[counter] = list_to_mute[counter]*2

        # check if list contains bool
        if type(list_to_mute[counter]) == bool:
            # if the bool is True, change it to false
            if list_to_mute[counter] is True:
                list_to_mute[counter] = False
            # if the bool is False, change it to True
            else:
                list_to_mute[counter] = True
        counter += 1
        # make first element of list into 'Hello'
        list_to_mute[0] = 'Hello'


def merge_dicts(dict1, dict2):
    '''(dict, dict) -> dict
    REQ: Both dicts should contain atleast 1 item (key and value)
    REQ: dict values must be int

    >>> a = {'yo': [1,2,3], 'ok': [1]}
    >>> b = {'yo': [1,2,3], 'ok': [1]}
    >>> merge_dicts(a,b)
    {'yo': [1,2,3,1,2,3], 'ok': [1,1]}
    >>> merge_dicts(b,a)
    {'yo': [1,2,3,1,2,3], 'ok':[1,1]}

    >>> a = {'yo': [1,2,3], 'ok': [4]}
    >>> b = {'yo': [4]}
    >>> merge_dicts(a,b)
    {'yo': [1,2,3,4], 'ok': [4]}
    >>> merge_dicts(b,a)
    {'yo': [4,1,2,3], 'ok': [4]}

    >>> a = {'yo': [1,2,3], 'ok':[4,5]}
    >>> b = {'ok': [2]}
    >>> merge_dicts(a,b)
    {'yo': [1,2,3], 'ok': [4,5,2]}
    >>> merge_dicts(b,a)
    {'yo': [1,2,3], 'ok': [2,4,5]}
    '''
    dict3 = dict()
    values = list()
    keys1 = list()
    keys2 = list()
    new_dict1 = dict()
    new_dict2 = dict()
    values2 = list()
    new = list()
    store = list()
    counter = 0

    # Find both keys of the dicts
    for akey in dict1.keys():
        keys1 += [akey]
    for keys in dict2.keys():
        keys2 += [keys]
    # Add the keys
    keys_total = keys1 + keys2
    # Remove the same keys
    for keys in keys_total:
        if keys not in new:
            new.append(keys)
    # If the keys exist in both dict1 and dict2, then combine their values
    # and put into new dict
    for keys in new:
        if ((keys in keys1) and (keys in keys2)):
            values = dict1[keys]
            values2 = dict2[keys]
            total = values + values2
            dict3[keys] = total
    # Find the keys of the new dict
    holder = dict3.keys()
    # Now remove the keys that are already in the final dict
    for keys in holder:
        if keys in new:
            new.remove(keys)
    # Now find the unique keys and turn into a serperate dict
    for keys in new:
        # If the keys are from dict1, then find the values and turn into dict
        if keys in keys1:
            values = dict1[keys]
            new_dict1[keys] = values

        # If keys are from dict2, then fing the values and turn into dict
        elif keys in keys2:
            values = dict2[keys]
            new_dict2[keys] = values

    # Now combine the 2 dictionaries together to form the changed dict
    dict4 = dict3.copy()
    dict4.update(new_dict1)
    dict4.update(new_dict2)
    return dict4
