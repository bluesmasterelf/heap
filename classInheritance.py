"""This module contains several ntuple classes meant to mimic all the properties of ntuples in R^n
<, > and * are all overloaded to accept dictionary ordering and scalar multiplication
"""
from math import sqrt, sin, cos, atan2, pi 
from heap import Heap, MedianHeap
from compareHeap import CompareHeap
import copy 

class Ntuple(object):
    """Had this lovely tuple class, then discovered the existing tuple structure. This ntuple structure is specifically meant to do everything that n-ntuples in R^n do
    """
    def __init__(self, dimension=None, initData=None):
        self.dimension=dimension
        self.ntuple=initData
    
    #Operator overloading experiment; dictionary order greater than and less than

    def __gt__(self, object):  #in dictionary order
        for i in range(0, self.dimension):    
            if self.ntuple[i]>object.ntuple[i]:
                return True
            elif self.ntuple[i]<object.ntuple[i]:
                return False
        return False #case of equality

    def __lt__(self, object):
        for i in range(0, self.dimension):    
            if self.ntuple[i]<object.ntuple[i]:
                return True
            elif self.ntuple[i]>object.ntuple[i]:
                return False
        return False #equality

    def __rmul__(self, integer):
        temp=copy.copy(self)
        for i in range(0, self.dimension):
            temp.ntuple[i]=self.ntuple[i]*integer
        return temp

    def __mul__(self, integer):
        temp=copy.copy(self)
        for i in range(0, self.dimension):
            temp.ntuple[i]=self.ntuple[i]*integer
        return temp

    def __add__(self, other):
        temp=copy.copy(self)
        for i in range(0, self.dimension):
            temp.ntuple[i]+=other.ntuple[i]
        return temp

class OrderedPair(Ntuple):
    def __init__(self, initData):
        Ntuple.__init__(self, 2, initData)
        self.polar=[sqrt(self.ntuple[0]**2+self.ntuple[1]**2),atan2(self.ntuple[1], self.ntuple[0])%(2*pi)] #range of atan2 is (-pi,pi]

    def getPolar(self):
        return self.polar
 


def polarGreater(pair1, pair2):
    """Function to compare ordered pairs in the polar dictionary order r, theta. Originally intended to pass to a heap or other sorting structure to sort OrderedPair objects. For polarLess, just use not polarGreater(1,2) after checking equality
    """
    r1, t1=pair1.getPolar()
    r2, t2=pair2.getPolar()
    if r1<r2:
        return False
    elif r1==r2:
        if t1<=t2:
            return False
        else:
            return True
    else:
        return True

class Triple(Ntuple):
    def __init__(self, initData):
        Ntuple.__init__(self, 3, initData)
        #self.spherical=function to convert to spherical
        #self.cylindrical=...

class Fourtle(Ntuple):
    def __init__(self, initData):
        Ntuple.__init__(self, 4, initData)
        #self.parallelized= negate second and forth coords


if __name__=='__main__':

#track their median in dictionary order x,y, test the operator overload
    maxHeap=Heap()
    compareHeap=CompareHeap(1, polarGreater)
    medHeap=MedianHeap()
#generate pairs
    testHeap=input('Do you want to test the heap? y/n')
    if testHeap=='y':
        for i in range(-2, 2):
            for j in range(-2, 2):
                test=OrderedPair([j,i])
                
                print('our newest addition is:')
                print (test.ntuple)
                
                medHeap.addElement(test)
                maxHeap.addElement(test)
                bestTuple=maxHeap.getMax()
                medTuple=medHeap.getMedian()
                print('the running max is:')
                print(bestTuple.ntuple)
                print('the running median is:')
                print(medTuple.ntuple)

    testCompare=input('Do you want to test the comparison function in a heap? y/n')
    if testCompare=='y':
        for i in range(-2, 2):
            for j in range(-2, 2):
                test=OrderedPair([j,i])
                print('The newest point in polar is: ')
                print(test.getPolar())
            
                compareHeap.addElement(test)
                bestPolar=compareHeap.getMax()
                print('The running max in polar coordinates is: ')
                print(bestPolar.getPolar())



#track their median in dictionary order r, theta
    #polarMedian=MedianHeap(polarGreater) #requires MedianHeap to accept comparison function
