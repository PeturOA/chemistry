#coding: utf-8
from element import Element, TableOfElements

class Atom(object):
    """An OOP representation of an Atom"""
    def __init__(self, **kwargs):
        # Number of protons (róteindir)
        self.no_protons = kwargs.get('no_protons')

        # Number of neutrons (nifteindir)
        default_ne = int(round(self.element.mass_number
                               - self.no_protons))
        self.no_neutrons = kwargs.get('no_neutrons', default_ne)

        # Number of electrons (rafeindir)
        self.no_electrons = kwargs.get('no_electrons', self.no_protons)

        self.position = kwargs.get('position', (0, 0, 0))
        self.velocity = kwargs.get('velocity', (0, 0, 0))
        
    @property
    def charge(self):
        return self.no_protons - self.no_electrons
        
    @property
    def mass(self):
        return self.no_protons + self.no_neutrons

    @property
    def element(self):
        return Element.get(self.no_protons)

    def __repr__(self):
        s = "{element} atom. P/N/E: {P}/{N}/{E}"
        return s.format(element=self.element,
                        P = self.no_protons,
                        N = self.no_neutrons,
                        E = self.no_electrons)

    

    



    @property
    def isotope(self):
        ## TODO
        return self.mass
