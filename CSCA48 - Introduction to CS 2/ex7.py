def edit_distance(s1, s2, numb_moves=0):
    '''(str, str) -> int
    REQ: len(s1) == len(s2)
    REQ: both s1 and s2 are non-empty

    >>> edit_distance('za', 'za')
    0

    >>> edit_distance('zain', 'aaaa')
    3

    Return the number of changes it would take for str1 to turn into str2.
    '''
    # If both strings are empty, then return 0
    if len(s1) == 0 and len(s2) == 0:
        return 0
    # check if length of s1 and s2 is not than 1, then continue:
    if len(s1) != 1 and len(s2) != 1:
        # if the first elements in each str are not the same, then increase
        # number of moves by 1.
        if s1[0] != s2[0]:
            numb_moves += 1
        # recurse next elements of each list and the number of moves
        return edit_distance(s1[1:], s2[1:], numb_moves)
    # if the length of both s1 and s2 is 1, then:
    else:
        # check if first elements of each lists are not equal
        if s1[0] != s2[0]:
            # if not equal, then increase number of moves by 1
            numb_moves += 1
        # lastly, return the number of moves
        return numb_moves


def subsequence(s1, s2):
    '''(str, str) -> bool
    REQ: len(s1) <= len(s2)
    REQ: length of s1 and s2 have to be greater than 1

    >>> subsequence('kking', 'yoyokidng')
    False

    >>> subsequence('zain', 'zaid')
    False

    >>> subsequence('aa', 'bbabba')
    True

    Return if s1 can be found in s2 in order.
    '''
    # while s1 has length greater than 1 and less than or equal to s2, continue
    if len(s1) <= len(s2) and len(s1) > 1:
        # if first element of s1 lies in s2, recurse and move to the next
        # element in s1.
        if s1[0] == s2[0]:
            return subsequence(s1[1:], s2[1:])

        else:
            # If the first element is not equal to s2 element 1, then return
            # the next element of s2 and check it
            return subsequence(s1[:], s2[1:])

    # No need to delete, since you cant delete, return False
    if len(s1) == 0 and len(s2) == 0:
        return False
    # Once s1 has a length of 1, check if the final element lies in s2.
    else:
        return s1 in s2


def perms(string):
    '''(str) -> set
    REQ: length of string is greater than 0

    >>> perms('ap')
    {'pa', 'ap'}

    >>> perms('zain')
    {'niza', 'izan', 'inaz', 'aniz', 'nzai', 'izna', 'ainz', 'zian', 'znia',
    'anzi', 'azni', 'azin', 'naiz', 'znai', 'iazn', 'inza', 'nzia', 'nazi',
    'zina', 'zani', 'niaz', 'ianz', 'zain', 'aizn'}

    >>> perms('ok')
    {'ok', 'ko'}

    >>> perms('aab')
    {'aab', 'aba', 'baa'}

    >>> perms('aaa')
    {'aaa'}

    Return the total number of possible computations/permutations of the
    string in a set. The set will remove all the duplicates.
    '''
    # Keep reducting the string, until it reaches base case of 1
    # return the string
    if len(string) == 1:
        return {string}
    # Base case can be 1 or less than 1
    # return the string
    if len(string) < 1:
        return {string}
    # Initialize for finding permutations
    # get each first element of the string and put it into remaining
    # words in all possible ways
    final, things_changed, first_word = list(), perms(string[1:]), string[0]
    # Starting from the end, take each element and make all possible perms
    for changes in things_changed:
        # append the word taken word into the words in each possible way
        # this way the number of permutations are formed
        for counter in range(len(changes) + 1):
            # ------------TEST-----------
            count = 10
            # print (counter)
            # ---------------------------
            final.append(changes[counter:] + first_word + changes[:counter])
    # Turn the list into a set, this way all the duplicates are removed
    # and the permutations are now stored in a set
    return set(final)
