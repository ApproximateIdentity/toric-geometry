import unittest
from numpy import array

import src.functional.area as area

class TestAreaFunction(unittest.TestCase):

    def setUp(self):
        self.triangle = [array([0,0]), array([1,0]), array([0,1])]
        self.square = [array([0,0]), array([1,0]), array([0,1]), array([1,1])]

    def test_area1(self):
        # Make sure area is correct for triangle.
        self.assertEqual(area(self.triangle), 0.5)

    def test_area2(self):
        # Make sure area is correct for square.
        self.assertEqual(area(self.square), 1.0)


if __name__=='__main__':
    unittest.main()
