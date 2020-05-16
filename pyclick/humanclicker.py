import pyautogui
import math as Math
import random
from pyclick.humancurve import HumanCurve


def setup_pyautogui():
    # Any duration less than this is rounded to 0.0 to instantly move the mouse.
    pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
    # Minimal number of seconds to sleep between mouse moves.
    pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
    # The number of seconds to pause after EVERY public function call.
    pyautogui.PAUSE = 0.015  # Default: 0.1

setup_pyautogui()


class HumanClicker():
    
    def __init__(self):
        pass

    def move_to_point(self, toPoint, duration=2, humanCurve=None):
        fromPoint = pyautogui.position()
        if not humanCurve:
            humanCurve = HumanCurve(fromPoint, toPoint)

        pyautogui.PAUSE = duration / len(humanCurve.points)
        for point in humanCurve.points:
            pyautogui.moveTo(point)

    def move_to_rect(self, x, y, w, h, duration=2, humanCurve=None):
        random_x = random.randint(x, x + w)
        random_y = random.randint(y, y + h)
        self.move_to_point((random_x, random_y), duration)

    def move_to_ellipse(self, ellipseOriginPoint, width, height, doRandomScale=True, duration=2, humanCurve=None):
        # Randomise the scale of the ellipse (between 0x and 1x scale)
        w = width
        h = height
        if doRandomScale == True:
            random_scale_multiplier = random.random()
            w = width * random_scale_multiplier
            h = height * random_scale_multiplier
        # Randomise an angle in radians between 0 and 2pi
        angle = Math.tau * random.random()
        # Find x and y positions on the ellipse at the given angle
        x = (w*h*Math.sin(angle)) / Math.sqrt((h*Math.cos(angle))**2 + (w*Math.sin(angle))**2)
        y = (w*h*Math.cos(angle)) / Math.sqrt((h*Math.cos(angle))**2 + (w*Math.sin(angle))**2)
        # Calculate final mouse point and move to that point
        toPoint = (int(round(x + ellipseOriginPoint[0])), int(round(y + ellipseOriginPoint[1])))
        self.move_to_point(toPoint, duration)

    def click(self, button="left", clicks=1, interval=0.15):
        pyautogui.click(button=button, clicks=clicks, interval=interval)
