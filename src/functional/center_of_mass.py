import numpy as np
from numpy import linalg

from src.functional.decompose import decompose_to_triangles
from src.functional.area import find_area_of_polygon

"""
Module for finding center of mass of convex polytopes.
"""

def center_of_mass(vertices):
    """
    Return center of mass of polygon spanned by vertex list.

    Parameters
    ----------
    vertices : N x 2 np.ndarray

    Returns
    -------
    center : 1 x 2 np.ndarray
    """
    center = np.array([0, 0], dtype='float')
    area = find_area_of_polygon(vertices)
    decomposition = decompose_to_triangles(vertices)

    for triangle in decomposition:
        area_of_triangle = find_area_of_polygon(triangle)
        center_of_triangle = find_center_of_mass_triangle(triangle)
        center += area_of_triangle*center_of_triangle
    
    center = (1/area)*center

    return center

def find_center_of_mass_triangle(vertices):
    """
    Return center of mass of triangle with vertices point1, point2 and point3.

    Parameters
    ----------
    vertices : 3 x 2 np.ndarray

    Returns
    -------
    center : 1 x 2 np.ndarray
    """
    V0 = vertices[0]
    V1 = vertices[1]
    V2 = vertices[2]
    M0 = 0.5*(V1 + V2)
    M1 = 0.5*(V0 + V2)

    M = np.array([M1 - V1, V0 - M0])
    parameters = (V0 - V1).dot(linalg.inv(M))
    t = parameters[1]
    center = V0 + t*(M0 - V0)

    return center
