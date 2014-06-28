import random
import unittest

from atom import *

gold = Element.get(79)
class TestAtom(unittest.TestCase):
	
	def setUp(self):
		pass
	
	def test_Hydrogen_constructor(self):
		H = Atom(no_protons=1)
		self.assertEqual(H.no_protons, 1)
		
	def test_Oxygen_constructor(self):
		O = Atom(no_protons=8)
		self.assertEqual(O.no_protons, 8)

if __name__ == '__main__':
	unittest.main()
