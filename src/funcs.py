"""Exercises with simple functions"""


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    return a * b * c


a = 6


def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    756
    """
    c = 3
    return a * b * c


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    return x if len(x) > len(y) else y


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    2.83
    """
    x1, y1 = p1
    x2, y2 = p2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
