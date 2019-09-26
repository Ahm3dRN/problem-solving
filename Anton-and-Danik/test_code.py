import unittest
from code import main

class TestStringMethods(unittest.TestCase):

	def setUp(self):
		self.samples = [
			# n , s, output
            [6, "ADAAAA", "Anton"],
            [7, "DDDAADA", "Danik"],
            [6, "DADADA", "Friendship"]
        ]

	def test_main(self):
		for sample in self.samples:
			self.assertEqual(main(sample[0], sample[1]), sample[2])

if __name__ == '__main__':
	unittest.main()