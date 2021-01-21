
class Heap3:
    def __init__(self):
        self.list = [0, None]

    def downHeap(self, i, n):
        smaller = i
        left = 2*i
        right = 2*i+1
        
        if left <= n and self.list[left] < self.list[smaller]:
            smaller = left
        if right <= n and self.list[right] < self.list[smaller]:
            smaller = right
        if smaller != i:
            self.list[i], self.list[smaller] = self.list[smaller], self.list[i]
            self.downHeap(smaller, n)

    def insert(self, keys, n):
        for i in keys:
            if self.list[1] == None:
                self.list[1] = int(i)
            else: 
                self.list.append(int(i))
        
        for i in range(n//2, 0, -1):
            self.downHeap(i, n)

    def Hprint(self, sorted):
        for i in sorted:
            print(i, end=" ")
        print()

    def heapSort(self, n):
        print(self.list)
        res = []
        for i in range(1,n+1,3):
            print("i = %d %d" %(i, self.list[i]))
            res.append(self.list[i])
            if 2*i>=n and 2*i+1>=n:
                break
            if self.list[2*i] < self.list[2*i+1]:
                res.append(self.list[2*i])
            if self.list[2*i] > self.list[2*i+1]:
                res.append(self.list[2*i+1])

        self.Hprint(res)


  

h = Heap3()
n = int(input())
keys = input().split()
h.insert(keys, n)
print(h.list)
h.heapSort(n)
