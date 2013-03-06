import unittest
from numpy import array

import src.functional.decompose as decompose

class TestAreaFunction(unittest.TestCase):

    def setUp(self):
        self.triangle = [array([0,0]), array([1,0]), array([0,1])]
        self.square = [array([0,0]), array([1,0]), array([0,1]), array([1,1])]

    def test_decompose1(self):
        # Make sure decompose returns triangle if given triangle.
        self.assertTrue(False)

    def test_area2(self):
        # Make sure decompose returns correct decomposition for square.
        self.assertTrue(False)


if __name__=='__main__':
    unittest.main()
