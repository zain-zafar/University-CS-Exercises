class LightSwitch():
    # Made to turn switch "on" or "off"
    # Initialize the class fuctions, where this function allows us
    # to use self, as a reference to other functions of the class
    def __init__(self, state):
        '''(LightSwitch, str) -> NoneType
        REQ: state == "on" or state == "off"
        This method will initialize the state of the switch, so that
        if state is "on" then make it equal to True
        if state is "off" then make it equal to False
        '''
        # If the state of the switch is "on", then make the state True
        if (state == "on"):
            # Make a class method, that the rest of the functions can refer to
            self.state = state
            self.state = True
        # IF the state of the switch is "off", then make the state False
        elif (state == "off"):
            # Make a class method, that the rest of the functions can refer to
            self.state = state
            self.state = False

    def turn_on(self):
        ''' Will turn on the switch'''
        # if switch is off then turn it on
        if (self.state is False):
            self.state = True
        else:
            # if switch is already on, then do nothing
            return

    def turn_off(self):
        '''This method will turn off the switch'''
        # Used to turn "off" a switch if it is on
        if (self.state is True):
            self.state = False
        else:
            # If switch is off, then do nothing.
            return

    def flip(self):
        '''This method will flip the state of the switch
        So, if the state is on, turn it off
        if state of switch is off, then turn it on'''
        # If the state of switch is True, then change to False
        if (self.state is True):
            self.state = False
        # If the state of switch is False, then change to True
        elif (self.state is False):
            self.state = True

    def __str__(self):
        '''This function will output a message depending on the
        state of the switch'''
        # If the state of the switch is "on", then return "I am on"
        if (self.state is True):
            return "I am on"
        # If the state of the switch is "off", then return "I am off"
        elif (self.state is False):
            return "I am off"


class SwitchBoard():
    def __init__(self, numb_of_swtches):
        '''(SwitchBoard, int) -> NoneType
        REQ: numb_of_swtches > 0
        Initialize the number of switches the user enters, by making them
        all False/off.
        '''
        # Increase number of switches by 1, because 0 is also a switch, so
        # Add 1 more switch to the given value.
        self.numb_of_swtches = numb_of_swtches
        # Make a new list which holds the number of closed switches.
        list_of_bool = self.numb_of_swtches*[False]
        # Create a reference variable
        self.list_of_bool = list_of_bool

    def which_switch(self):
        '''This method will find all the switches in the list which
        are True'''
        list_of_int = list()
        counter = 0
        # Loop through the list of switches
        for counter in range(len(self.list_of_bool)):
            # Find all the switches that are on
            if (self.list_of_bool[counter] == True):
                # Store all those switches in a list of int
                list_of_int.append(counter)
            counter += 1
        return list_of_int

    def flip(self, wht_to_flip):
        '''(SwitchBoard, int) -> NoneType
        REQ: wht_to_flip should exist inside the list of switches
        REQ: wht_to_flip >= 0
        Flip the n'th switch given in the list of switches.
        '''
        # As long as the value needed to be flipped lies in the len
        # of the list_of_bool, then continue:
        if (wht_to_flip in range(len(self.list_of_bool))):
            # Find the value at the given index inside list_of_bool
            flip_this = self.list_of_bool[wht_to_flip]
            # If that value is True, then flip it to False
            if (flip_this is True):
                # change that value in the list of bool, to false
                self.list_of_bool[wht_to_flip] = False
            # If the value of switch to flip is 0, then only flip that
            # switch
            elif (wht_to_flip == 0):
                self.list_of_bool[wht_to_flip] = not (self.list_of_bool
                                                      [wht_to_flip])
            else:
                # Flip the switch to True, if the value is False
                self.list_of_bool[wht_to_flip] = True
        # If the value, needed to be flipped isnt in range of the list,
        # then do nothing...
        else:
            return

    def flip_every(self, wht_to_flip):
        '''(SwitchBoard, int) -> NoneType
        REQ: wht_to_flip >= 0
        Flip the nth switch and every n'th switch, including the first switch.
        NOTE: first switch which is the 0th switch will always be flipped.
        '''
        # As long as the counter lies in len of list_of_bool
        # Cycle thorugh the list of bool, by starting at 0,
        # and going up by increments of the n item needed to be flipped
        if (wht_to_flip != 0):
            for counter in range(0, len(self.list_of_bool), wht_to_flip):
                # Flip the item and flip it, and return the list
                SwitchBoard.flip(self, counter)
        # if the given flip value is 0, then dont do anything
        elif wht_to_flip == 0:
            pass

    def __str__(self):
        '''This method will output all the switches that are on'''
        # Refer back to SwitchBoard method which_switch in order to
        # generate a list of all the switches which are on...
        lister = SwitchBoard.which_switch(self)
        # Convert the new list of int to list of str, in order to use .join
        counter = 0
        while (counter < len(lister)):
            # Turn all the int elements into str elements
            lister[counter] = str(lister[counter])
            counter += 1
        # Convert the list of str to str
        convert_lst_to_str = ' '.join(lister)
        return "The following switches are on: "+convert_lst_to_str

    def reset(self):
        '''Makes all the switches off/False'''
        # Overwrite the self list, in order to make all of its values
        # false, which means every switch is now off/False
        self.list_of_bool = len(self.list_of_bool)*[False]

# ------------------GLOBAL TESTING------------------------
# Checks if the file we are running is the main file
if __name__ == "__main__":
    # Generate 1024 switches, all from 0-1023
    test = SwitchBoard(1024)
    # Now as long as counter is in range of the number of switches,
    # flip every other switch in such a way that the steps given to
    # solve the problem are working.
    for counter in range(1, 1024):
        # Flip every second switch, then every third switch and so on..
        SwitchBoard.flip_every(test, counter)
    # Print the value, to see what the result is
    print(test)
# Judging from the output, I can say that ONLY perfect square switches
# will be on
