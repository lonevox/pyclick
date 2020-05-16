import unittest
from pyclick.humanclicker import HumanClicker
import pyautogui
import random


class TestHumanClicker(unittest.TestCase):

    def test_simple(self):
        width, height = pyautogui.size()
        to_point = (width//2, height//2)
        hc = HumanClicker()
        hc.move(to_point)
        self.assertTrue(pyautogui.position() == to_point)

    def test_identity_move(self):
        to_point = pyautogui.position()
        hc = HumanClicker()
        hc.move(to_point)
        self.assertTrue(pyautogui.position() == to_point)

    def test_random_move(self):
        width, height = pyautogui.size()
        to_point = random.randint(width//2,width-1), random.randint(height//2,height-1)
        hc = HumanClicker()
        hc.move(to_point)
        self.assertTrue(pyautogui.position() == to_point)
