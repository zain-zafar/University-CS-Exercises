class queue:
    ''' A class to represent a container'''

    def __init__(self):
        self._cont = list()

    def put(self, item):
        self._cont.append(item)

    def is_empty(self):
        return (len(self._cont) == 0)

    def get(self):
        if(queue.is_empty(self) == False):
            return (self._cont.pop(0))
        else:
            raise ContainerEmptyException

    def peek(self):
        if(queue.is_empty(self) == False):
            element = self._cont[0]
            return element
        else:
            raise ContainerEmptyException

class stack:
    ''' A class to represent a container'''

    def __init__(self):
        self._cont = list()

    def put(self, item):
        self._cont.append(item)

    def is_empty(self):
        return (len(self._cont) == 0)

    def get(self):
        if(stack.is_empty(self) == False):
            return (self._cont.pop(len(self._cont)-1))
        else:
            raise ContainerEmptyException

    def peek(self):
        if(stack.is_empty(self) == False):
            element = self._cont[0]
            return element
        else:
            raise ContainerEmptyException

class bucket:
    ''' A class to represent a container'''

    def __init__(self):
        self._cont = list()

    def put(self, item):
        if(bucket.is_empty(self) == True):
            self._cont.append(item)
        else:
            raise ContainerFullException

    def is_empty(self):
        return (len(self._cont) == 0)

    def get(self):
        if(bucket.is_empty(self) == False):
            return (self._cont.pop(0))
        else:
            raise ContainerEmptyException

    def peek(self):
        if(bucket.is_empty(self) == False):
            element = self._cont[0]
            return element
        else:
            raise ContainerEmptyException

class ContainerEmptyException(Exception):
    '''A class for empty container exception'''
    pass

class ContainerFullException(Exception):
    '''A class for container full exception'''
    pass