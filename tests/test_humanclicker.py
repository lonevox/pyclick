import unittest
import pyclick.humanclicker
import pyautogui
import random


class TestHumanClicker(unittest.TestCase):

    def test_simple(self):
        width, height = pyautogui.size()
        to_point = (width//2, height//2)
        humanclicker.move_to_point(to_point)
        self.assertTrue(pyautogui.position() == to_point)

    def test_identity_move_to_point(self):
        to_point = pyautogui.position()
        humanclicker.move_to_point(to_point)
        self.assertTrue(pyautogui.position() == to_point)

    def test_random_move_to_point(self):
        width, height = pyautogui.size()
        to_point = random.randint(width//2,width-1), random.randint(height//2,height-1)
        humanclicker.move_to_point(to_point)
        self.assertTrue(pyautogui.position() == to_point)
