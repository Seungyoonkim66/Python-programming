class Heap:
    def __init__(self,keys):
        self.array = [0]+keys 
        
        
    def rBuildHeap(self,i):
        if i> len(self.array)-1:
            return 
        
        self.rBuildHeap(2*i)
        self.rBuildHeap(2*i+1)
        self.downHeap(i,len(self.array)-1)
        return 
        
    def buildHeap(self):
        for i in range((len(self.array)-1)//2,0,-1):
            self.downHeap(i,len(self.array)-1)
        return 
    
    def upHeap(self,i):
        if i ==1:
            return
        if self.array[i//2]>self.array[i]:
            return
        
        temp1 = self.array[i]
        temp2 = self.array[i//2]
        self.array[i]=temp2
        self.array[i//2]=temp1
        self.upHeap(i//2)
    
    def downHeap(self,i,last):
        if last < 2*i:
            return
        
        greater = 2*i
        if last>=2*i+1:
            if self.array[greater]<self.array[2*i+1]:
                greater = 2*i+1
        
        if self.array[i]>self.array[greater]:
            return
        
        temp1 = self.array[i]
        temp2 = self.array[greater]
        self.array[i] = temp2
        self.array[greater]=temp1
        self.downHeap(greater,last)
        
        
    def inplaceHeapSort(self,recursive):
        if recursive:
            self.rBuildHeap(1)
        else:
            self.buildHeap()
        
        for i in range(len(self.array)-1,1,-1):
            temp1 = self.array[1]
            temp2 = self.array[i]
            self.array[1]=temp2
            self.array[i]=temp1
            self.downHeap(1,i-1)
        
        
    def printHeap(self):
        assert len(self.array)>=2
        for key in self.array[1:]:
            print(key, end=' ')
            
        print("")
    
    def main(self,recursive=True):
        self.inplaceHeapSort(recursive)
        self.printHeap()
        return 
        
N= int(input())
keys = [int(i) for i in input().split()]    
a= Heap(keys)
a.main(recursive=False)