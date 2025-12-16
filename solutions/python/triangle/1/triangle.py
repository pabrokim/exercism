def equilateral(sides):
    """
    Determine whether a triangle is equilateral.

    parameters
    ---------------

    sides: list of int or float
    
    returns
    ----------------
    bool
        True if all sides are equal. False otherwise
    
    """
    
    #check lengths first then equate all sides
    
    return len(sides)==3 and all(side>0 for side in sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """
    Determine whether a triangle is isosceles.
    """

    if len(sides) != 3:
        return False

    # all sides must be positive
    for side in sides:
        if side <= 0:
            return False

    a, b, c = sides

    # triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # at least two sides equal
    return a == b or a == c or b == c


def scalene(sides):
    if len(sides) != 3:
        return False

    # all sides must be positive
    for side in sides:
        if side <= 0:
            return False

    a, b, c = sides

    # triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    # all sides must be different
    return a != b and a != c and b != c

