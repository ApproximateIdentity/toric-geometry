import numpy as np

"""
Module for performing one-dimensional integration of functions over lines in
the plane and two-dimensional integration of functions over triangles in the
plane.
"""

def integrate_over_line(function, point1, point2, weight):
    """
    Integrate function on line connecting point1 and point2 in plane and
    normalize so that the total mass of the line is weight.

    Parameters
    ----------
    function : real-valued function whose inputs are 2 x 1 np.ndarrays
    point1 : 2 x 1 np.ndarray
    point2 : 2 x 1 np.ndarray
    weight : postivie real number

    Returns
    -------
    w : real number
    """
    pass

def integrate_over_triangle(function, point1, point2, point3):
    """
    Integrate function over triangle with vertices given by point1, point2 and
    point2.

    Parameters
    ----------
    function : real-valued function whose inputs are 2 x 1 np.ndarrays
    point1 : 2 x 1 np.ndarray
    point2 : 2 x 1 np.ndarray
    point3 : 2 x 1 np.ndarray

    Returns
    -------
    w : real number
    """
    pass
