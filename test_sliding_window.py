import unittest
from sliding_window import sliding_window

class TestSlidingWindow(unittest.TestCase):
	def test_sliding_window(self):
		self.assertAlmostEqual(sliding_window())