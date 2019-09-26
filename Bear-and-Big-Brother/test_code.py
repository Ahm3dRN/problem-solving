import unittest
from code import main

class TestStringMethods(unittest.TestCase):

	def setUp(self):
		self.samples = [
			# n , s, output
            [4, 7, 2],
            [4, 9, 3],
            [1, 1, 1]
        ]

	def test_main(self):
		for sample in self.samples:
			self.assertEqual(main(sample[0], sample[1]), sample[2])

if __name__ == '__main__':
	unittest.main()