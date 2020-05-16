import unittest
import numpy as np
from pyclick._utils import is_numeric, is_list_of_points


class TestBezierCurve(unittest.TestCase):

    def test_is_numeric(self):
        self.assertTrue(is_numeric(1))
        self.assertTrue(is_numeric(1.0))
        self.assertTrue(is_numeric(np.int(0)))
        self.assertTrue(is_numeric(np.int32(0)))
        self.assertTrue(is_numeric(np.int64(0)))
        self.assertTrue(is_numeric(np.float64(2)))

    def test_is_not_numeric(self):
        self.assertFalse(is_numeric("asd"))
        self.assertFalse(is_numeric(None))
        self.assertFalse(is_numeric([]))
        self.assertFalse(is_numeric({}))
        self.assertFalse(is_numeric(set()))

    def test_is_list_of_points(self):
        self.assertTrue(is_list_of_points([]))
        self.assertTrue(is_list_of_points([
            (0, 0), (1.2, 2), (np.float32(2), np.int(0))
        ]))
        self.assertTrue([
            [1,2.0]
        ])

    def test_is_not_list_of_points(self):
        self.assertFalse(is_list_of_points("asd"))
        self.assertFalse(is_list_of_points([
            (1, 2), ("asd", 3)
        ]))
        self.assertFalse(is_list_of_points([
            [None,None]
        ]))
        self.assertFalse(
            is_list_of_points([2,2])
        )
        self.assertFalse(is_list_of_points(None))
