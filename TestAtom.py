import random
import unittest

from atom import *

gold = Element.get(79)
class TestAtom(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_constructor_valid_element(self):
        try:
            Atom(no_protons=1).element
            Atom(no_protons=118).element
        except:
            self.fail()
    
    def test_constructor_invalid_element(self):
        with self.assertRaises(ValueError):
            Atom(no_protons=-200)
        with self.assertRaises(ValueError):
            Atom(no_protons=-1)
        with self.assertRaises(ValueError):
            Atom(no_protons=0).element
        with self.assertRaises(ValueError):
            Atom(no_protons=119).element
        with self.assertRaises(ValueError):
            Atom(no_protons=200).element
        with self.assertRaises(ValueError):
            Element.get(-200)
        with self.assertRaises(ValueError):
            Element.get(-1)
        with self.assertRaises(ValueError):
            Element.get(0)
        with self.assertRaises(ValueError):
            Element.get(119)
        with self.assertRaises(ValueError):
            Element.get(200)
    
    def test_Hydrogen_constructor(self):
        H = Atom(no_protons=1)
        self.assertEqual(H.no_protons, 1)
        
    def test_Oxygen_constructor(self):
        O = Atom(no_protons=8)
        self.assertEqual(O.no_protons, 8)
            
    def test_random_atoms(self):
        for r in xrange(1,119):
            atom = Atom(no_protons=r)
            self.assertTrue(type(atom.no_protons) == int)
            self.assertTrue(atom.no_protons > 0)
            self.assertTrue(type(atom.no_neutrons) == int)
            self.assertTrue(atom.no_neutrons >= 0)
            self.assertTrue(type(atom.no_electrons) == int)
            self.assertTrue(atom.no_electrons >= 0)
            self.assertEqual(atom.no_protons, r)
            self.assertTrue(type(atom.mass) == int)
            self.assertTrue(atom.mass >= 0)
            self.assertTrue(atom.mass == atom.no_protons+atom.no_neutrons)
            self.assertTrue(type(atom.element.symbol) == str)
            self.assertFalse(atom.element.symbol == '')
            self.assertTrue(type(atom.element.name) == str)
            self.assertFalse(atom.element.name == '')
            self.assertTrue(type(atom.element.atomic_number) == int)
            self.assertTrue(atom.element.atomic_number >= 1)
            self.assertTrue(atom.element.atomic_number <= 118)
            self.assertTrue(atom.element.atomic_number == r)
            self.assertTrue(atom.element.atomic_number == atom.no_protons)
            self.assertTrue(type(atom.element.mass_number) == float)
            self.assertTrue(atom.element.mass_number > 0)
            

if __name__ == '__main__':
    unittest.main()
