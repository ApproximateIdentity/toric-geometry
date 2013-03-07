import unittest
from numpy import array
from numpy.testing.utils import assert_equal

from src.functional.decompose import decompose_to_triangles

class TestDecompose(unittest.TestCase):

    def setUp(self):
        self.triangle1 = array([[0, 0], [1, 0], [0, 1]], dtype='float')
        self.triangle2 = array([[0, 0], [2, 0], [0, 1]], dtype='float')
        self.square = array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype='float')
        self.trapezoid = array([[0, 0], [2, 0], [1, 1], [0, 1]], dtype='float')
        self.pentagon = array([[0, 0], [2, 0], [2, 1], [1, 2], [0, 2]],
                              dtype='float')

    def test_decompose_triangle1(self):
        # Make sure decompose returns same thing if given a triangle.
        result = decompose_to_triangles(self.triangle1)
        benchmark = array([[[0, 0], [1, 0], [0, 1]]], dtype='float')
        assert_equal(result, benchmark)

    def test_decompose_triangle2(self):
        # Make sure decompose returns same thing if given another triangle.
        result = decompose_to_triangles(self.triangle2)
        benchmark = array([[[0, 0], [2, 0], [0, 1]]], dtype='float')
        assert_equal(result, benchmark)

    def test_decompose_square(self):
        # Make sure decompose returns correct thing for a square.
        result = decompose_to_triangles(self.square)
        benchmark = array([[[0, 0], [1, 0], [1, 1]],
                           [[0, 0], [1, 1], [0, 1]]], dtype='float')
        assert_equal(result, benchmark)

    def test_decompose_trapezoid(self):
        # Make sure decompose returns correct thing for a trapezoid.
        result = decompose_to_triangles(self.trapezoid)
        benchmark = array([[[0, 0], [2, 0], [1, 1]],
                           [[0, 0], [1, 1], [0, 1]]], dtype='float')
        assert_equal(result, benchmark)

    def test_decompose_pentagon(self):
        # Make sure decompose returns correct thing for a pentagon.
        result = decompose_to_triangles(self.pentagon)
        benchmark = array([[[0, 0], [2, 0], [2, 1]],
                           [[0, 0], [2, 1], [1, 2]],
                           [[0, 0], [1, 2], [0, 2]]], dtype='float')
        assert_equal(result, benchmark)


if __name__=='__main__':
    unittest.main()
