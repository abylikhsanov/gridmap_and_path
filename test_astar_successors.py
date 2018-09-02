import unittest
from new_astar import Node

class TestCases(unittest.TestCase):
	def test(self):
		# Test bottom left:
		node = Node(0,0,10,10)
		self.assertEqual(node.successors(10,10), [(1,0),(1,1),(0,1)])

		# Test top left:
		node = Node(9,0,10,10)
		self.assertEqual(node.successors(10,10), [(),(),()])

		# Test top right:
		node = Node(9,9,10,10)
		self.assertEqual(node.successors(10,10), [(),(),()])

		# Test bottom right:
		node = Node(0,9,10,10)
		self.assertEqual(node.successors(10,10), [(),(),()])

		# Test left edge: