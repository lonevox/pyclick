import pytweening
import numpy as np
import random
from pyclick._utils import is_list_of_points, is_numeric
from pyclick._beziercurve import BezierCurve


class HumanCurve():
    """
    Generates a human-like mouse curve starting at given source point,
    and finishing in a given destination point
    """

    def __init__(self, from_point, to_point, **kwargs):
        self.from_point = from_point
        self.to_point = to_point
        self.points = self.generate_curve(**kwargs)

    def generate_curve(self, **kwargs):
        """
        Generates a curve according to the parameters specified below.
        You can override any of the below parameters. If no parameter is
        passed, the default value is used.
        """
        offset_boundary_x = kwargs.get("offset_boundary_x", 100)
        offset_boundary_y = kwargs.get("offset_boundary_y", 100)
        left_boundary = kwargs.get("left_boundary", min(self.from_point[0], self.to_point[0])) - offset_boundary_x
        right_boundary = kwargs.get("right_boundary", max(self.from_point[0], self.to_point[0])) + offset_boundary_x
        down_boundary = kwargs.get("down_boundary", min(self.from_point[1], self.to_point[1])) - offset_boundary_y
        up_boundary = kwargs.get("up_boundary", max(self.from_point[1], self.to_point[1])) + offset_boundary_y
        knots_count = kwargs.get("knots_count", 2)
        distortion_mean = kwargs.get("distortion_mean", 1)
        distortion_stdev = kwargs.get("distortion_stdev", 1)
        distortion_frequency = kwargs.get("distortion_frequency", 0.5)
        tween = kwargs.get("tweening", pytweening.easeOutQuad)
        target_points = kwargs.get("target_points", 100)

        internal_knots = self.generate_internal_knots(left_boundary,right_boundary, \
            down_boundary, up_boundary, knots_count)
        points = self.generate_points(internal_knots)
        points = self.distort_points(points, distortion_mean, distortion_stdev, distortion_frequency)
        points = self.tween_points(points, tween, target_points)
        return points

    def generate_internal_knots(self, \
        left_boundary, right_boundary, \
        down_boundary, up_boundary,\
        knots_count):
        """
        Generates the internal knots used during generation of bezier curve_points
        or any interpolation function. The points are taken at random from
        a surface delimited by given boundaries.
        Exactly knots_count internal knots are randomly generated.
        """
        if not (is_numeric(left_boundary) and is_numeric(right_boundary) and
            is_numeric(down_boundary) and is_numeric(up_boundary)):
            raise ValueError("Boundaries must be numeric")
        if not isinstance(knots_count, int) or knots_count < 0:
            raise ValueError("knots_count must be non-negative integer")
        if left_boundary > right_boundary:
            raise ValueError("left_boundary must be less than or equal to right_boundary")
        if down_boundary > up_boundary:
            raise ValueError("down_boundary must be less than or equal to up_boundary")

        knots_x = np.random.choice(range(left_boundary, right_boundary), size=knots_count)
        knots_y = np.random.choice(range(down_boundary, up_boundary), size=knots_count)
        knots = list(zip(knots_x, knots_y))
        return knots

    def generate_points(self, knots):
        """
        Generates bezier curve points on a curve, according to the internal
        knots passed as parameter.
        """
        if not is_list_of_points(knots):
            raise ValueError("knots must be valid list of points")

        mid_pts_cnt = max( \
            abs(self.from_point[0] - self.to_point[0]), \
            abs(self.from_point[1] - self.to_point[1]), \
            2)
        knots = [self.from_point] + knots + [self.to_point]
        return BezierCurve.curve_points(mid_pts_cnt, knots)

    def distort_points(self, points, distortion_mean, distortion_stdev, distortion_frequency):
        """
        Distorts the curve described by (x,y) points, so that the curve is
        not ideally smooth.
        Distortion happens by randomly, according to normal distribution,
        adding an offset to some of the points.
        """
        if not(is_numeric(distortion_mean) and is_numeric(distortion_stdev) and \
               is_numeric(distortion_frequency)):
            raise ValueError("Distortions must be numeric")
        if not is_list_of_points(points):
            raise ValueError("points must be valid list of points")
        if not (0 <= distortion_frequency <= 1):
            raise ValueError("distortion_frequency must be in range [0,1]")

        distorted = []
        for i in range(1, len(points)-1):
            x,y = points[i]
            delta = np.random.normal(distortion_mean, distortion_stdev) if \
                random.random() < distortion_frequency else 0
            distorted += (x,y+delta),
        distorted = [points[0]] + distorted + [points[-1]]
        return distorted

    def tween_points(self, points, tween, target_points):
        """
        Chooses a number of points(tween_points) from the list(points)
        according to tweening function(tween).
        This function in fact controls the velocity of mouse movement
        """
        if not is_list_of_points(points):
            raise ValueError("points must be valid list of points")
        if not isinstance(target_points, int) or target_points < 2:
            raise ValueError("target_points must be an integer greater or equal to 2")

        # tween is a function that takes a float 0..1 and returns a float 0..1
        res = []
        for i in range(target_points):
            index = int(tween(float(i)/(target_points-1)) * (len(points)-1))
            res += points[index],
        return res
