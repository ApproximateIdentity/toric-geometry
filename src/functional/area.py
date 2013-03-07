import numpy as np
from numpy import linalg

"""
Module for finding area of a polygon.
"""

def area(vertex_list):
    """
    Return area of polygon.

    Parameters
    ----------
    vertex_list : N x 2 np.ndarray

    Returns
    -------
    area : real number
    """
    area = area_of_triangle(vertex_list)
    return area

def area_of_triangle(vertex_list):
    """
    Return area of triangle.

    Parameters
    ----------
    vertex_list : 3 x 2 np.ndarray

    Returns
    -------
    area : real number
    """
    # Use determinant.
    M = np.vstack((vertex_list.T, np.array([1, 1, 1], dtype='float')))
    area = 0.5*linalg.det(M)
    return area
