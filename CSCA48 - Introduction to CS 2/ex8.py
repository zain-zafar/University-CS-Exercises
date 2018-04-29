class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, initial_depth):
        '''(BBTNode, int) -> NoneType
        '''
        # Set the initial given depth as the BBT depth
        self.depth = initial_depth
        # Set the counter to 1 plus the depth of BBT
        counter = self.depth + 1

        # if both children are not empty of the root, then increase both of
        # their depth to counter
        if self.left is not None and self.right is not None:
            self.left.set_depth(counter)
            self.right.set_depth(counter)

        # If only left child exists, then change its depth to counter
        elif self.left is not None and self.right is None:
            self.left.set_depth(counter)

        # if only right child exists, change its depth to counter
        elif self.right is not None and self.left is None:
            self.right.set_depth(counter)

    def leaves_and_internals(self, node=set(), leaves=set(), root=False):
        '''(BTNode) -> tuple(set, set)
        REQ: A BBT has been created

        Return the leaves and internals in 2 seperate sets, in a tuple.
        '''
        # check if the binary tree at the root have both left and right
        # children
        if self.left is not None and self.right is not None:
            # As long as the optional parameter is False, the root will not
            # be considered a part of the tree and will not be recursed on
            # IF root is true, meaning it is a valid node, then continue
            if root:
                # add the node into the internals set
                node.add(self.value)
                # Recurse to the left child of this node, setting the root
                # to true, since every node now is valid part of the BT
                self.left.leaves_and_internals(node, leaves, True)
                # Do the same for the right side of the tree
                self.right.leaves_and_internals(node, leaves, True)

            else:
                # If the object is not a node, then do not add to set and
                # recurse left and right of it
                self.left.leaves_and_internals(node, leaves, True)
                self.right.leaves_and_internals(node, leaves, True)

        # if the left child exists but not the right child
        elif self.left is not None and self.right is None:
            # consider this node as a parent and add it to interals set, but
            # only add iff root is True
            if root is True:
                node.add(self.value)
            # recurse to the left child
            self.left.leaves_and_internals(node, leaves, True)

        # if the right child eists, but not the left child
        elif self.right is not None and self.left is None:
            # add the node value to the internals set, iff root is True
            if root is True:
                node.add(self.value)
                self.right.leaves_and_internals(node, leaves, True)
            # recurse to the right child of this node
            self.right.leaves_and_internals(node, leaves, True)

        # If no children of the node exist, add the node value to the set of
        # leaves, iff root == True
        elif self.right is None and self.left is None:
            leaves.add(self.value)

        # return the set of leaves and the set of internals as a tuple
        return (leaves, node)

    def sum_to_deepest(self, counter=0, lister=list()):
        '''(BTNode) -> int
        REQ: BT has been created

        Return the max depth of the tree
        '''
        # If no children exist, then return the depth of 0
        if self.right is None and self.left is None:
            return counter
        # But if children exist, then:
        else:
            # Increase depth by 1
            counter = counter + 1
            # Append the counter value into a list
            lister.append(counter)
            # If both children exist, set their depth to counter
            if self.right is not None and self.left is not None:
                # recurse the right tree first and keep going right, while
                # increasing the counter as the depth increases
                self.right.sum_to_deepest(counter, lister)
                # Do the same for the left subtree, and as more nodes are found
                # increase their depth to counter
                self.left.sum_to_deepest(counter, lister)
            # If only the right child exists
            elif self.left is None and self.right is not None:
                # then increase and set the depth to counter of only right
                # child
                self.right.sum_to_deepest(counter, lister)
            # If only left child exists, then set the left child to depth of
            # counter, and keep going left.
            elif self.right is None and self.left is not None:
                self.left.sum_to_deepest(counter, lister)
            # Using the max method in python, get the highest depth value
            # in the list
            return max(lister)

# --------------------------------------------------------------------------
if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(1000, None, None), BTNode(100, None, None))
    print(my_tree)
    my_tree.set_depth(0)
    print(my_tree.leaves_and_internals())
    print(my_tree.sum_to_deepest())
