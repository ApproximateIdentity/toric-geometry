import numpy as np

"""
Module for decomposing vertex points into lines and triangles.
"""

def decompose_to_edges(vertex_points):
    """
    Return list of pairs of adjacent vertices coming from list of vertex
    points.

    Parameters
    ----------
    vertex_points : N x 2 np.ndarray

    Returns
    -------
    edges_list : length N list of pairs of np.ndarrays
    """
    pass

def decompose_to_triangles(vertex_points, base_point=None):
    """
    Return list of triples of points which form triangles. The first point in
    each triple is base_point.

    Parameters
    ----------
    vertex_points : N x 2 np.ndarray
    base_point : 1 x 2 np.ndarray

    Returns
    -------
    triangles_list : length N or (N-2) list of triples of np.ndarrays

    Notes
    -----
    If base_point is None, then base_point is set as vertex_points[0].
    Consequently, there are only N-2 triangles left since two of them would
    have area 0.
    """
    pass
