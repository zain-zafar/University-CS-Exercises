import math
ninty_angle = 90


# Create a Parent class, which all the other classes can refer to
class ParentShape():

    def __init__(self, base, side, theta):
        '''(ParentShape, float, float, float) -> NoneType
        REQ: base > 0, side > 0
        REQ: 0 < theta < 180
        Initialize all the vairables, and make sure they are float
        '''
        self.base = base
        self.side = side
        self.theta = theta

    # Convert the given angle into degrees and then apply math.sin
    # this will allow for the use of theta to find area of shape
    def area(self):
        ''''Return area of shape'''
        conv_to_deg = math.radians(self.theta)
        find_sin = math.sin(conv_to_deg)
        area = self.base*self.side*find_sin
        return area

    # Return all the variables of the shape in the order: base, side, theta
    def bst(self):
        return [self.base, self.side, self.theta]


# Create a shape class: Parallelogram
class Parallelogram(ParentShape):

    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> NoneType
        REQ: base > 0, side > 0
        REQ: 0 < theta < 180
        Initialize the variables given using Parent class
        '''
        ParentShape.__init__(self, base, side, theta)

    def __str__(self):
        '''Return a message with area of Parallelogram'''
        return "I am a Parallelogram with area "+str(ParentShape.area(self))


# Create a new shape class: Rectangle
class Rectangle(ParentShape):

    def __init__(self, base, side):
        '''(Rectangle, float, float) -> NoneType
        REQ: base >0 and side > 0
        Initialize the variables given using Parent class
        '''
        theta = ninty_angle  # Make the angle of shape always be 90 degrees
        ParentShape.__init__(self, base, side, theta)

    def __str__(self):
        '''Return a message with the area of the Rectangle '''
        return "I am a Rectangle with area "+str(ParentShape.area(self))


# Create a new shape class: Rhombus
class Rhombus(ParentShape):

    def __init__(self, base, theta):
        '''(Rhombus, float, float) -> NoneType
        REQ: base > 0
        REQ: 0 < theta < 180
        Initialize the variables given using Parent class
        '''
        side = base  # Create a side which is the same value as base
        ParentShape.__init__(self, base, side, theta)

    # Return a message with the area of the Square
    def __str__(self):
        '''Return a message with the area of the Rhombus'''
        return "I am a Rhombus with area of "+str(ParentShape.area(self))


# Create a new shape class: Square
class Square(ParentShape):

    def __init__(self, base):
        '''(Square, float) -> NoneType
        REQ: base > 0
        Initialize the variables given using Parent class
        '''
        side = base  # create a side, with same value as base
        theta = ninty_angle  # make theta always equal to 90.
        ParentShape.__init__(self, base, side, theta)

    def __str__(self):
        '''Return a message with the area of the Square'''
        return "I am a Square with area of "+str(ParentShape.area(self))
