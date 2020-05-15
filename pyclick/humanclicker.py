import pyautogui
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

    def click(self, button="left", clicks=1, interval=0.15):
        pyautogui.click(button=button, clicks=clicks, interval=interval)
