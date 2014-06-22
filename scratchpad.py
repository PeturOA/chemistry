from atom import *
from random import randint

l = [Atom(no_protons=randint(1, 118)) for _ in range(20)]
for a in l:
    print " -", a
