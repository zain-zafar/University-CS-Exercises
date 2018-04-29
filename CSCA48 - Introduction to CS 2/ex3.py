from container import *


def banana_verify(source_word, goal_word, container, list_of_moves):
    '''(str, str, Container, list) -> bool
    REQ: len(source_word) > 0
    REQ: len(goal_word) > 0
    REQ: list_of_moves must have only 'M','G','P'
    REQ: len(list_of_moves) >= 0

    >>> banana_verify("BANANA", "AAANNB", stack(),
    ["P","M","P","M","P","M","G","G","G"])
    True

    >>> banana_verify("BANANA", "AAANNBATMAN", stack(), ["P", "G"])
    False

    >>> banana_verify("BANANA","AAABBN", bucket(), ["M", "G"])
    False

    >>> banana_verify("BANANA","NABANA", queue(),
    ['P','P','M','M','G','G','M','M'])
    True

    Returns True iff the word created after applying list_of_moves given
    is the same as goal_word. If the word created is not the same as the
    goal_word, then return False.
    '''
    # this str will turn into a word, as moves are applies to it
    formed_word = str()
    gg = container()
    # if an exception error is raised, then return false
    try:
        # for each word in the list of moves
        for moves in list_of_moves:
            # if moves are equal to 'P'
            if moves == 'P':
                # store the first letter from the word, which is to be Put
                # into container
                stored_letter = source_word[0]
                # make the source word equal to everything except the
                # first letter
                source_word = source_word[1:]
                # put the letter into container
                gg.put(stored_letter)
            # if the move is 'M', then
            elif moves == 'M':
                # store first letter from source_word
                word_to_move = source_word[0]
                # Remove the first letter from source_word
                source_word = source_word[1:]
                # add the letter at the end of formed_word
                formed_word += word_to_move
            # if move is 'G', which is Get, then get next word from container
            elif moves == 'G':
                # get word from container and store it
                get_word = gg.get()
                # add that word to end of formed_word
                formed_word += get_word
        # if the formed_word is the same as goal_word, then return True
        if formed_word == goal_word:
            return True
        else:
            return False
    # if an error occurs, make sure code does not crash, instead returns False
    except:
        return False
