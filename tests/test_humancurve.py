import unittest
import pytweening
from pyclick.humanclicker import HumanCurve


class TestHumanCurve(unittest.TestCase):

    def test_generate_curve(self):
        from_point = (100,100)
        to_point = (1000,1000)
        hc = HumanCurve(from_point, to_point)
        points = hc.generate_curve(offset_boundary_x=10, offset_boundary_y=50,\
            left_boundary=10, right_boundary=1000, \
            down_boundary=10, up_boundary=1000, \
            knots_count=5, \
            distortion_mean=10, distortion_stdev=5, distortion_frequency=0.5, \
            tween=pytweening.easeOutCubic, \
            target_points=100)

        self.assertTrue(len(points) == 100)
        self.assertTrue(points[0] == from_point)
        self.assertTrue(points[-1] == to_point)

    def test_generate_internal_knots(self):
        from_point = (100,100)
        to_point = (1000,1000)
        hc = HumanCurve(from_point, to_point)

        lb, rb, db, ub = 10, 20, 30, 40
        knots_count = 5
        internal_knots = hc.generate_internal_knots(lb,rb,db,ub, knots_count)
        self.assertTrue(len(internal_knots) == knots_count)
        for knot in internalKnots:
            self.assertTrue(lb <= knot[0] <= rb)
            self.assertTrue(db <= knot[1] <= ub)

    def test_generate_points(self):
        from_point = (99,99)
        to_point = (100,100)
        hc = HumanCurve(from_point, to_point)

        lb, rb, db, ub = 10, 20, 30, 40
        knots_count = 5
        internal_knots = hc.generate_internal_knots(lb,rb,db,ub, knots_count)
        points = hc.generate_points(internal_knots)

        self.assertTrue(len(points) >= 2)
        self.assertTrue(points[0] == from_point)
        self.assertTrue(points[-1] == to_point)

    def test_distort_points(self):
        points = [(1,1), (2,1), (3,1), (4,1), (5.5,1)]
        copy_points = [pt for pt in points]
        from_point, to_point = (1,1), (2,1)
        hc = HumanCurve(from_point, to_point)
        distorted = hc.distort_points(points, 0,0,0)
        self.assertTrue(distorted == copy_points)

    def test_tween_points(self):
        points = [(i,1) for i in range(100,111)]
        copy_points = [pt for pt in points]
        from_point, to_point = (1,1), (2,1)
        hc = HumanCurve(from_point, to_point)

        target_points = 11
        tween_constant_fun = lambda x : 0.5
        tweened = hc.tween_points(points, tween_constant_fun, target_points)
        self.assertTrue(len(tweened) == target_points)
        self.assertTrue(tweened == [points[5] for _ in range(target_points)])
