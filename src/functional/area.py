import numpy as np
from numpy import linalg

from src.functional.decompose import decompose_to_triangles

"""
Module for finding area of a polygon.
"""

def area(vertex_points):
    """
    Return area of polygon.

    Parameters
    ----------
    vertex_points : N x 2 np.ndarray

    Returns
    -------
    area : real number
    """
    decomposition = decompose_to_triangles(vertex_points)
    area = 0.0
    for triangle in decomposition:
        area += area_of_triangle(triangle)
    return area

def area_of_triangle(vertex_points):
    """
    Return area of triangle.

    Parameters
    ----------
    vertex_points : 3 x 2 np.ndarray

    Returns
    -------
    area : real number
    """
    # Use determinant.
    M = np.vstack((vertex_points.T, np.array([1, 1, 1], dtype='float')))
    area = 0.5*linalg.det(M)
    return area
