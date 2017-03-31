"""We have here a basic heap structure in the class Heap. It is structured as a max heap, and accepts a -1 to convert to a min heap for real number inputs. The class MedianHeap is a solution to the common median-tracker problem, and implements an instance of each a max and min heap. In the main program, functionality is tested. """

import operator

class Heap:
    """This is a basic heap data-structure. 
    """
    def __init__(self, comparison=operator.gt):  #FIX  delete reverse, integrate choose function. 
        self.data=[]
        self.comparison=comparison

    def __len__(self):
        return len(self.data)

    def addElement(self, number):
        self.data.append(number)  #percolate up
        
        isSorted=False
        tempIdx = len(self.data)-1
        while not isSorted:
           
            parentIdx=int(tempIdx/2)

            if self.comparison(self.data[tempIdx], self.data[parentIdx]):
                self.data[tempIdx], self.data[parentIdx]=self.data[parentIdx], self.data[tempIdx] 
                tempIdx=int(tempIdx/2)
            else:
                isSorted=True


    def getMax(self):
        return self.data[0]

    def pop(self):
        """This function pops the max (min) and then restores the binary tree structure.
        """

        if len(self.data)==0:
            raise IndexError('pop from empty heap')

        tempIdx=0
        biggerIdx=1

#FIX  if empty, should throw index error: empty heap

        while 2*tempIdx < len(self.data):
            if self.comparison(self.data[2*tempIdx-1], self.data[2*tempIdx]):
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


class MedianHeap: 
    """This structure accepts numbers and tracks their median value. 
    """
    def __init__(self):
        self.maxHeap=Heap()
        self.minHeap=Heap(operator.lt)
        self.balancedState=0	#-1,0 or 1 depending if minHeap has 1 more, equal or one less than the maxHeap
        self.isEmpty=True

    def addElement(self, element):
        if self.isEmpty:
            self.minHeap.addElement(element)
            self.balancedState-=1
            self.isEmpty=False
            self.median=element
        
        elif element<self.getMedian():
            self.maxHeap.addElement(element)
            self.balancedState+=1
        else:
            self.minHeap.addElement(element)
            self.balancedState-=1

#balance the two heaps if necessary
        if self.balancedState<-1:
            self.maxHeap.addElement(self.reverseHeap.pop())
            self.balancedState+=2
        if self.balancedState>1:
            self.minHeap.addElement(self.maxHeap.pop())
            self.balancedState-=2

    def getBalancedState(self):
        return self.balancedState

    def getMedian(self):
        if self.balancedState==1:
            return self.maxHeap.getMax()
        elif self.balancedState==-1:
            return self.minHeap.getMax()
        else: 
            return (self.minHeap.getMax()+self.maxHeap.getMax())*0.5


	 


if __name__=='__main__':

#maxHeap test
    print('testing maxHeap')
    myMaxHeap=Heap()
    for i in range(4):
        myMaxHeap.addElement(i)
        print (myMaxHeap.getMax())
    myMaxHeap.addElement(7)
    print (myMaxHeap.getMax())
    print (len(myMaxHeap))

    myMaxHeap.pop()
    print (myMaxHeap.getMax())

#    for i in range(5):
#        print(myMaxHeap.pop())
#Testing pop exception 


#minHeap test
    print('testing minHeap, should produce 7,6,5,4')
    myMinHeap=Heap(operator.lt)
    for i in range(4):
        myMinHeap.addElement(7-i)
        print (myMinHeap.getMax())


#medianHeap test

    print('will now print running median over test scores')

    myTestScores=[87,27,66,55,44,75,81]
    testMedian=MedianHeap()
    print (myTestScores)
    for score in myTestScores:
        testMedian.addElement(score)
        print ('balancedState:', testMedian.getBalancedState())
        print ('median:', testMedian.getMedian())
        print ('minHeap:', testMedian.minHeap.data[0])
        print('next iterate')
		  
