import random


class Heap(object):
    '''A class representing a heap.'''

    def __init__(self, insert_list=[]):
        '''(Heap, list) -> NoneType
        Create a new Heap containing the elements in insert_list.
        '''

        self._heap = []
        if(len(insert_list) > 0):
            for element in insert_list:
                self.insert(element)

    def is_empty(self):
        '''(Heap) -> bool
        Return True iff there are no nodes in this Heap.
        '''

        return (len(self._heap) == 0)

    def insert(self, insert_value):
        '''(Heap, object) -> NoneType
        Insert insert_value into this Heap.
        REQ: insert_value is not already in this Heap.
        '''
        if insert_value in self._heap:
            pass
        else:
            self._heap += [insert_value]
            self.bubble_up(len(self._heap) - 1)

    def bubble_up(self, c_index):
        '''(Heap, int) -> NoneType

        Re-arrange the values in this Heap to maintain the heap
        property after a new element has been inserted into the
        heap. The offending child node is located at c_index.
        '''

        p_index = (c_index) // 2
        # Base Case: We're at the beginning of the list, do nothing
        if c_index > 0:
            if self._heap[p_index] < self._heap[c_index]:
                # swap the parent and child
                self.swap(c_index, p_index)
                # RD: bubble up again from our new position
                self.bubble_up(p_index)

    def swap(self, i, j):
        '''(Heap, int, int) -> NoneType
        Swap the values at indices i and j.
        '''
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def remove_top(self):
        '''(Heap) -> object
        Remove and return the largest element in this Heap.
        RAISES: HeapEmptyException if this Heap is empty.
        '''

        if len(self._heap) == 0:
            raise HeapEmptyError("Attempt to remove top of empty heap")
        else:
            # save the top element
            ret = self._heap[0]
            # remove the last element from the heap, and
            # replace the head's value with it
            last = self._heap.pop()
            if len(self._heap) > 0:
                self._heap[0] = last
                self.bubble_down(0)
            return ret

    def bubble_down(self, p_index):
        '''(Heap) -> NoneType

        Re-arrange the values in this Heap to maintain the heap
        property after the top element of the heap has been removed.
        The parent node which potentially violates the heap property
        is located at p_index.
        '''

        lt_index = (p_index * 2) + 1
        rt_index = (p_index * 2) + 2
        # Base Case: If we don't violate, then do nothing
        if self.violates(p_index):
            # one of our children violates the heap property
            # if we only have a left child, it must be that one
            if rt_index >= len(self._heap):
                self.swap(p_index, lt_index)
                p_index = lt_index

            # if we have two children, we need to swap with the larger child
            elif self._heap[lt_index] > self._heap[rt_index]:
                self.swap(p_index, lt_index)
                p_index = lt_index
            else:
                self.swap(p_index, rt_index)
                p_index = rt_index
            # RD: Bubble down from our new position
            self.bubble_down(p_index)

    def violates(self, index):
        '''(Heap, int) -> bool

        Return whether the node at index and one of its children
        violate the heap property.
        '''

        lt_index = (index * 2) + 1
        rt_index = (index * 2) + 2
        # if we have no children, we're fine
        if lt_index >= len(self._heap):
            return False
        # if we have one child, return True iff it violates
        elif rt_index >= len(self._heap):
            return self._heap[lt_index] > self._heap[index]
        # if we have two children, return True if either child violates
        else:
            return (self._heap[lt_index] < self._heap[index] or
                    self._heap[rt_index] < self._heap[index])


if __name__ == "__main__":
    my_unordered_list = []
    random_number = random.random() * 100
    for i in range(10):
        my_unordered_list.append(random_number)
    my_heap = Heap(my_unordered_list)
    # print(my_heap)
    my_ordered_list = []
    while not my_heap.is_empty():
        my_ordered_list.append(my_heap.remove_top())
        # print(my_heap)
    print(my_ordered_list)
