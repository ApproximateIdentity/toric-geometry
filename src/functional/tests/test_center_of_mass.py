import unittest
from numpy import array
from numpy.testing.utils import assert_allclose

from src.functional.center_of_mass import center_of_mass

class TestDecompose(unittest.TestCase):

    def setUp(self):
        self.triangle1 = array([[0, 0], [1, 0], [0, 1]], dtype='float')
        self.triangle2 = array([[0, 0], [2, 0], [0, 1]], dtype='float')
        self.square = array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype='float')
        self.trapezoid = array([[0, 0], [2, 0], [1, 1], [0, 1]], dtype='float')
        self.pentagon = array([[0, 0], [2, 0], [2, 1], [1, 2], [0, 2]],
                              dtype='float')

    def test_com_triangle1(self):
        # Make sure center of mass works right for a triangle.
        result = center_of_mass(self.triangle1)
        benchmark = array([1.0/3.0, 1.0/3.0], dtype='float')
        assert_allclose(result, benchmark)

    def test_com_triangle2(self):
        # Make sure center of mass works right for another triangle.
        result = center_of_mass(self.triangle2)
        benchmark = array([2.0/3.0, 1.0/3.0], dtype='float')
        assert_allclose(result, benchmark)

    def test_com_square(self):
        # Make sure center of mass works right for a square.
        result = center_of_mass(self.square)
        benchmark = array([1.0/2.0, 1.0/2.0], dtype='float')
        assert_allclose(result, benchmark)

    def test_com_trapezoid(self):
        # Make sure center of mass works right for a trapezoid.
        result = center_of_mass(self.trapezoid)
        benchmark = array([7.0/9.0, 4.0/9.0], dtype='float')
        assert_allclose(result, benchmark)

    def test_com_pentagon(self):
        # Make sure center of mass works right for a pentagon.
        result = center_of_mass(self.pentagon)
        benchmark = array([19.0/21.0, 19.0/21.0], dtype='float')
        assert_allclose(result, benchmark)


if __name__=='__main__':
    unittest.main()
