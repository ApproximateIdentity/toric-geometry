import unittest
from numpy import array

from src.functional.area import area

class TestAreaFunction(unittest.TestCase):

    def setUp(self):
        self.triangle1 = array([[0, 0], [1, 0], [0, 1]], dtype='float')
        self.triangle2 = array([[0, 0], [2, 0], [0, 1]], dtype='float')
        self.square = array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype='float')
        self.trapezoid = array([[0, 0], [2, 0], [0, 1], [1, 1]], dtype='float')
        self.pentagon = array([[0, 0], [2, 0], [2, 1], [1, 2], [0, 2]],
                              dtype='float')

    def test_area_triangle1(self):
        # Make sure area is correct for triangle.
        self.assertEqual(area(self.triangle1), 0.5)

    def test_area_triangle2(self):
        # Make sure area is correct for another triangle.
        self.assertEqual(area(self.triangle2), 1.0)

    def test_area_square(self):
        # Make sure area is correct for square.
        self.assertEqual(area(self.square), 1.0)

    def test_area_trapezoid(self):
        # Make sure area is correct for trapezoid.
        self.assertEqual(area(self.trapezoid), 1.5)

    def test_area_pentagon(self):
        # Make sure area is correct for pentagon.
        self.assertEqual(area(self.pentagon), 3.5)


if __name__=='__main__':
    unittest.main()
