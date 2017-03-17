"""Attempting to code a max pile"""
from array import *

class maxHeap:
    def __init__(self):
        self.data=array('i', [])
		 #would like to implement with List of objects which can compare themselves
		 #There are self comparing tuples in classInheritance.py	 

    def __len__(self):
        return len(self.data)

    def addElement(self, number):
        self.data.append(number)
    #percolate up
        isSorted=False
        tempIdx = len(self.data)-1
        while not isSorted:
            if tempIdx%2==0:
                if self.data[tempIdx]>self.data[tempIdx/2]:
                    self.data[tempIdx], self.data[tempIdx/2]=self.data[tempIdx/2], self.data[tempIdx] 
                    tempIdx=tempIdx/2
                else:
                    isSorted=True
            else: 
                if self.data[tempIdx]>self.data[(tempIdx-1)/2]:
                    self.data[tempIdx], self.data[(tempIdx-1)/2]=self.data[(tempIdx-1)/2], self.data[tempIdx]
                    tempIdx=(tempIdx-1)/2
                else:
                    isSorted=True

    def getMax(self):
        return self.data[0]

    def pop(self):
        tempIdx=1
        biggerIdx=2
        while 2*tempIdx < len(self.data):
            if self.data[2*tempIdx-1]>self.data[2*tempIdx]:
                biggerIdx=2*tempIdx
            else:
                biggerIdx=2*tempIdx+1 #default right in the event of equality, doesn't matter unless terminal element...
                self.data[tempIdx-1]=self.data[biggerIdx-1] #drop larger value down
                tempIdx=biggerIdx #move into subtree

            #still need to sift down to fill a vacancy (probably), still have biggeridx
            for i in range(len(self.data)-biggerIdx-1):
                self.data[biggerIdx]=self.data[biggerIdx+i]
			   #WARNING!! Have not proofed indexing
                self.data.pop()
                return self.data[0]

class minHeap:
    def __init__(self):
        self.data=array('i', [])
		 #would like to implement with List of objects which can compare themselves
		 #There are self comparing tuples in classInheritance.py	 

    def __len__(self):
        return len(self.data)

    def addElement(self, number):
        self.data.append(number)
        #percolate up
        isSorted=False
        tempIdx = len(self.data)-1
        while not isSorted:
            if tempIdx%2==0:
                if self.data[tempIdx]<self.data[tempIdx/2]:
                    self.data[tempIdx], self.data[tempIdx/2]=self.data[tempIdx/2], self.data[tempIdx] 
                    tempIdx=tempIdx/2
                else:
                    isSorted=True
            else: 
                if self.data[tempIdx]<self.data[(tempIdx-1)/2]:
                    self.data[tempIdx], self.data[(tempIdx-1)/2]=self.data[(tempIdx-1)/2], self.data[tempIdx]
                    tempIdx=(tempIdx-1)/2
                else:
                    isSorted=True

    def getMin(self):
        return self.data[0]

    def pop(self):
        tempIdx=1
        biggerIdx=2
        while 2*tempIdx < len(self.data):
            if self.data[2*tempIdx-1]<self.data[2*tempIdx]:
                biggerIdx=2*tempIdx
            else:
                biggerIdx=2*tempIdx+1 #default right in the event of equality, doesn't matter unless terminal element...
                self.data[tempIdx-1]=self.data[biggerIdx-1] #drop larger value down
                tempIdx=biggerIdx #move into subtree

        #still need to sift down to fill a vacancy (probably), still have biggeridx
        for i in range(len(self.data)-biggerIdx-1):
            self.data[biggerIdx]=self.data[biggerIdx+i]
			   #WARNING!! Have not proofed indexing
        self.data.pop()
        return self.data[0]


class medianHeap: 
    def __init__(self):
        self.maxHeap=maxHeap()
        self.minHeap=minHeap()
        self.balancedState=0	#-1,0 or 1 depending if minHeap has 1 more, equal or one less than the maxHeap
        self.median=0.0

    def addElement(self, element):
        if element<self.getMedian():
            self.maxHeap.addElement(element)
            self.balancedState+=1
        else:
            self.minHeap.addElement(element)
            self.balancedState-=1

#balance the two heaps if necessary
        if self.balancedState<-1:
            self.maxHeap.addElement(self.minHeap.pop())
            self.balancedState+=2
        if self.balancedState>1:
            self.minHeap.addElement(self.maxHeap.pop())
            self.balancedState-=2

#adjust median to account
        if self.balancedState==1:
            self.median= self.maxHeap.getMax()
        elif self.balancedState==-1:
            self.median= self.minHeap.getMin()
        else: 
            self.median=(self.minHeap.getMin()+self.maxHeap.getMax())/float(2)
 

    def getBalancedState(self):
        return self.balancedState

    def getMedian(self):
        return self.median

	 


if __name__=='__main__':

#maxHeap test
    print('testing maxHeap')
    myMaxHeap=maxHeap()
    for i in range(4):
        myMaxHeap.addElement(i)
        print myMaxHeap.getMax()
    myMaxHeap.addElement(7)
    print myMaxHeap.getMax()
    print len(myMaxHeap)

    myMaxHeap.pop()
    print myMaxHeap.getMax()


#minHeap test
    print('testing minHeap, should produce 7,6,5,4')
    myMinHeap=minHeap()
    for i in range(4):
        myMinHeap.addElement(7-i)
        print myMinHeap.getMin()


#medianHeap test

    print('will now print running median over test scores')

    myTestScores=[87,27,66,55,44,75,81]
    testMedian=medianHeap()
    print myTestScores
    for score in myTestScores:
        testMedian.addElement(score)
        print 'balancedState:', testMedian.getBalancedState()
        print 'median:', testMedian.getMedian()
        print 'minHeap:', testMedian.minHeap.data[0]
        print('next iterate')
		  
