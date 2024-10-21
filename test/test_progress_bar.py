import os
from datetime import datetime
from PIL import Image, ImageDraw
import unittest
import glob
import sys

sys.path.insert(0, 'src')
from progress_bar import generate_progress_bar




class TestStringMethods(unittest.TestCase):
    def test_progress_bar_result(self):
        files = glob.glob(fr"test\media\*")
        for f in files:
            os.remove(f)
        for i in range(0, 101):
            current_time = datetime.now().strftime(f"%Y-%m-%d_%H_%M")
            self.assertEqual(generate_progress_bar(i,"test\\media"),fr"test\media\progress_{current_time}_{float(i):.1f}.png")

if __name__ == '__main__':
    unittest.main()