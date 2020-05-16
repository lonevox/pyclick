import pyautogui
import math as Math
import random
import time
from pyclick.humancurve import HumanCurve


def setup_pyautogui():
    # Any duration less than this is rounded to 0.0 to instantly move the mouse.
    pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
    # Minimal number of seconds to sleep between mouse moves.
    pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
    # The number of seconds to pause after EVERY public function call.
    pyautogui.PAUSE = 0.015  # Default: 0.1

setup_pyautogui()


def move_to_point(to_point, duration=2, human_curve=None):
    from_point = pyautogui.position()
    if not human_curve:
        human_curve = HumanCurve(from_point, to_point)

    pyautogui.PAUSE = duration / len(human_curve.points)
    for point in human_curve.points:
        pyautogui.moveTo(point)


def move_to_rect(x, y, w, h, duration=2, human_curve=None):
    random_x = random.randint(x, x + w)
    random_y = random.randint(y, y + h)
    move_to_point((random_x, random_y), duration, human_curve)


def move_to_ellipse(ellipse_origin_point, width, height, do_random_scale=True, duration=2, human_curve=None):
    # Randomise the scale of the ellipse (between 0x and 1x scale)
    w = width
    h = height
    if do_random_scale == True:
        random_scale_multiplier = random.random()
        w = width * random_scale_multiplier
        h = height * random_scale_multiplier
    # Randomise an angle in radians between 0 and 2pi
    angle = Math.tau * random.random()
    # Find x and y positions on the ellipse at the given angle
    x = (w*h*Math.sin(angle)) / Math.sqrt((h*Math.cos(angle))**2 + (w*Math.sin(angle))**2)
    y = (w*h*Math.cos(angle)) / Math.sqrt((h*Math.cos(angle))**2 + (w*Math.sin(angle))**2)
    # Calculate final mouse point and move to that point
    to_point = (int(round(x + ellipse_origin_point[0])), int(round(y + ellipse_origin_point[1])))
    move_to_point(to_point, duration, human_curve)


def click(button="left", delay_range=(0, 0), clicks=1, interval=0.15):
    time.sleep(random.uniform(*delay_range))
    pyautogui.click(button=button, clicks=clicks, interval=interval)
