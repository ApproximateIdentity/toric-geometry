import numpy as np

"""
Module for decomposing vertex points into lines and triangles.
"""

def decompose_to_edges(vertices):
    """
    Return list of pairs of adjacent vertices coming from list of vertex
    points.

    Parameters
    ----------
    vertices : N x 2 np.ndarray

    Returns
    -------
    edges : N x 2 x 2 np.ndarray
    """
    pass

def decompose_to_triangles(vertices, base_point=None):
    """
    Return list of triples of points which form triangles. The first point in
    each triple is base_point.

    Parameters
    ----------
    vertices : N x 2 np.ndarray
    base_point : 1 x 2 np.ndarray

    Returns
    -------
    triangles : N x 3 x 2 or (N-2) x 3 x 2 dimensio np.ndarray

    Notes
    -----
    If base_point is None, then base_point is set as vertices[0].
    Consequently, there are only N -2 triangles left since two of them would
    have area 0.
    """
    num_vertices = len(vertices)
    triangles = np.array([vertices[0:3]])
    for i in range(2, num_vertices - 1):
        mask = [0, i, i+1]
        triangles = np.vstack((triangles, np.array([vertices[mask]])))

    return triangles
