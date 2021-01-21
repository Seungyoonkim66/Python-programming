class Heap:
    def __init__(self):
        self.array = [0,None]
        
    def insertItem(self,data):
        assert len(self.array)<100
        
        if self.array[1] ==None:
            self.array[1]=data
            
        else:
            self.array.append(data)
                    
        pointer = self.array[-1]
        self.upHeap(pointer)
        return 0
        
    def upHeap(self,pointer):
        if pointer ==self.array[1]:
            return

        pointer_index = self.array.index(pointer)
        if pointer < self.array[pointer_index//2]:
            return 
        
        # 부모 & pointer swapping
        self.array[pointer_index]=self.array[pointer_index//2]
        self.array[pointer_index//2] = pointer
        self.upHeap(self.array[pointer_index//2])
    
    def removeMax(self):
        root = self.array[1]
        if len(self.array)==2:
            self.array =[0,None]
            return root
        
        temp = self.array[-1]
        self.array.remove(root)
        self.array.remove(0)
        self.array.remove(temp)
        self.array = [0,temp] + self.array
        self.downHeap(self.array[1])
        return root
        
    def downHeap(self,pointer):
        assert pointer in self.array

        pointer_index = self.array.index(pointer)
        if (len(self.array)<=pointer_index*2)& \
            (len(self.array)<=pointer_index*2+1):
                return
            
        bigger = self.array[pointer_index*2]

        if (len(self.array)>pointer_index*2+1):
            if self.array[pointer_index*2+1] > bigger:
                bigger = self.array[pointer_index*2 +1]
                
        if pointer > bigger:
            return 
        
        bigger_index = self.array.index(bigger)
        
        self.array[pointer_index]=self.array[bigger_index]
        self.array[bigger_index] = pointer
        self.downHeap(self.array[bigger_index])
    
    def printData(self):
        for data in self.array[1:]:
            print(data,end=' ')
        print()
    
# i,d,p,q 네 가지 명령
H = Heap()

while True:
    order = input().split()
    if order[0] == 'i':
        print(H.insertItem(int(order[1])))

    elif order[0] == 'd':
        print(H.removeMax())

    elif order[0] == 'p':
        H.printData()
    elif order[0] == 'q':
        break
    else:
        break