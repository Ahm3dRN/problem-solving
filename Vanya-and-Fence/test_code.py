import unittest
from code import main

class TestStringMethods(unittest.TestCase):

	def setUp(self):
		self.samples = [
			# n , h, heights, output
            [3, 7 , [4, 5,14], 4],
            [6, 1, [1, 1, 1, 1, 1, 1], 6],
            [6, 5, [7, 6, 8, 9, 10, 5], 11]
        ]

	def test_main(self):
		for sample in self.samples:
			self.assertEqual(main(sample[0], sample[1], sample[2]), sample[3])

if __name__ == '__main__':
	unittest.main()