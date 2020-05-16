import unittest
from pyclick._beziercurve import BezierCurve


class TestBezierCurve(unittest.TestCase):

    def test_binomial(self):
        self.assertEqual(BezierCurve.binomial(10,2), 45)
        self.assertEqual(BezierCurve.binomial(4,2), 6)
        self.assertEqual(BezierCurve.binomial(1,1), 1)
        self.assertEqual(BezierCurve.binomial(2,0), 1)

    def test_bernstein_polynomial_point(self):
        self.assertEqual(BezierCurve.bernstein_polynomial_point(5,0,0), 1)

        self.assertEqual(BezierCurve.bernstein_polynomial_point(3, 0, 1), -2)
        self.assertEqual(BezierCurve.bernstein_polynomial_point(3, 1, 1), 3)

        self.assertEqual(BezierCurve.bernstein_polynomial_point(3, 0, 2), 4)
        self.assertEqual(BezierCurve.bernstein_polynomial_point(3, 1, 2), -12)
        self.assertEqual(BezierCurve.bernstein_polynomial_point(3, 2, 2), 9)

    def test_simple_bernstein_polynomial(self):
        bernstein_polynomial = BezierCurve.bernstein_polynomial([(0,0), (50,50), (100,100)])
        self.assertEqual(bernstein_polynomial(0), (0,0))
        self.assertEqual(bernstein_polynomial(0.25), (25, 25))
        self.assertEqual(bernstein_polynomial(0.5), (50, 50))
        self.assertEqual(bernstein_polynomial(0.75), (75, 75))
        self.assertEqual(bernstein_polynomial(1), (100,100))

    def test_complex_bernstein_polynomial(self):
        bernstein_polynomial = BezierCurve.bernstein_polynomial([(0,0), (40,40), (100,100)])
        self.assertEqual(bernstein_polynomial(0), (0,0))
        self.assertEqual(bernstein_polynomial(0.25), (21.25,21.25))
        self.assertEqual(bernstein_polynomial(0.5), (45,45))
        self.assertEqual(bernstein_polynomial(0.75), (71.25, 71.25))
        self.assertEqual(bernstein_polynomial(1), (100,100))

    def test_simple_curve_points(self):
        points = [(0,0), (50,50), (100,100)]
        n = 5
        expected_curve_points = [(0,0),(25,25),(50,50),(75,75),(100,100)]
        self.assertEqual(BezierCurve.curve_points(n, points), expected_curve_points)

    def test_complex_curve_points(self):
        points = [(0,0), (40,40), (100,100)]
        n = 5
        expected_curve_points = [(0,0),(21.25,21.25),(45,45),(71.25,71.25),(100,100)]
        self.assertEqual(BezierCurve.curve_points(n, points), expected_curve_points)
