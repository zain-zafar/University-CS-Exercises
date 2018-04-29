def radix_sort(main_bin):
    '''(list of int) -> list of int
    REQ: list contains all positive integers or 0

    >>> radix_sort([1,2,3,1,2,3,4,0,4])
    [0,1,1,2,2,3,3,4,4]

    Return a sorted list, using radix method
    '''

    # Initialize 10 bins
    bin_0, bin_1, bin_2, bin_3, bin_4 = [], [], [], [], []
    bin_5, bin_6, bin_7, bin_8, bin_9 = [], [], [], [], []

    # Find the number of largest digit place
    biggest = len(str(max(main_bin)))
    # Create a empty list
    holder = []
    # Make all elements the same length by adding zeros to the ones with length
    # less than biggest
    for i in main_bin:
        i = str(i)
        while len(i) != biggest:
            i = '0' + str(i)
        holder.append(i)

    # Starting from 1, all the way to the last values of the elements,
    # sort them into their bins
    for counter in range(1, biggest + 1):

        for elements in holder:
            store = elements[-counter]

            if store == '0':
                bin_0.append(elements)

            elif store == '1':
                bin_1.append(elements)

            elif store == '2':
                bin_2.append(elements)

            elif store == '3':
                bin_3.append(elements)

            elif store == '4':
                bin_4.append(elements)

            elif store == '5':
                bin_5.append(elements)

            elif store == '6':
                bin_6.append(elements)

            elif store == '7':
                bin_7.append(elements)

            elif store == '8':
                bin_8.append(elements)

            elif store == '9':
                bin_9.append(elements)

        # Set Main bin as the sum of the bins from 0 - 9
        main_bin = bin_0 + bin_1 + bin_2 + bin_3 + bin_4 +\
            bin_5 + bin_6 + bin_7 + bin_8 + bin_9
        # Set holder as the main bin
        holder = main_bin
        # Clear all the values inside the bins
        bin_0, bin_1, bin_2, bin_3, bin_4 = [], [], [], [], []
        bin_5, bin_6, bin_7, bin_8, bin_9 = [], [], [], [], []

    # Once all the digits have been checked and the elements have been placed
    # into bins, then turn the main bin into a list of int, which will
    # remove all the extra 0's
    main_bin = list(map(int, main_bin))

    # Return the sorted main bin
    return main_bin
