class Heap2:
    def __init__(self):
        self.list = [0, None]

    def downHeap(self, i, n):
        bigger = i
        left = 2*i
        right = 2*i+1
        #print("bigger = %d left = %d right = %d" %(bigger, left, right))
        if left <= n and self.list[left] > self.list[bigger]:
            bigger = left
        if right <= n and self.list[right] > self.list[bigger]:
            bigger = right
            #print("bogger = %d" %(self.list[bigger]))
        if bigger != i:
            self.list[i], self.list[bigger] = self.list[bigger], self.list[i]
            self.downHeap(bigger, n)

    def insert(self, keys, n):
        for i in keys:
            if self.list[1] == None:
                self.list[1] = int(i)
            else: 
                self.list.append(int(i))
        
        # 리프노드는 downheap하지 않아도 되니까 리프 노드의 부모노드부터 
        for i in range(n//2, 0, -1):
            self.downHeap(i, n)

    def print(self):
        for i in self.list[1:]:
            print(i, end=" ")
        print()
  

h = Heap2()
n = int(input())
keys = input().split()
h.insert(keys, n)
h.print()