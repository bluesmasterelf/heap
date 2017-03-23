"""This module contains a variety of tuple classes. It's primary purpose has been for the author's review of class inheritance. There are also some comparison functions to send to any manner of sorting structures elsewhere. 
"""
from math import sqrt, sin, cos 

class Tuple:
    """This is the rough architecture of all n-tuples. Qualities that depend on the dimension are relegated to those subclasses. 
    """
    def __init__(self, dimension=None, initData=None):
        self.dimension=dimension
        self.tuple=initData

#These operatore overloads are limited to dictionary order, need to write more robust comparison functions.
    def __gt__(self, object):  #in dictionary order
        for i in range(0, self.dimension):    
            if self.tuple[i]>object.tuple[i]:
                return True
            elif self.tuple[i]<object.tuple[i]:
                return False

    def __lt__(self, object):
        for i in range(0, self.dimension):    
            if self.tuple[i]<object.tuple[i]:
                return True
            elif self.tuple[i]>object.tuple[i]:
                  


class OrderedPair(tuple):
    """Class for (x,y) type objects. 
    """
    def __init__(self, initData):
        tuple.__init__(self, 2, initData)
         #self.polar=function to convert to polar coords, need to import NumPy?
     

class Triple(tuple):
    """Class for (x,y,z) type objects
    """
    def __init__(self, initData):
        tuple.__init__(self, 3, initData)
        #self.spherical=function to convert to spherical
        #self.cylindrical=...

class Fourtle(tuple):
    """Class for (x1,x2,x3,x4) type objects. 
    """
    def __init__(self, initData):
        tuple.__init__(self, 4, initData)
        #self.parallelized= negate second and forth coords


if __name__=='__main__':

#some test code, will probably test over in the heap file. 
