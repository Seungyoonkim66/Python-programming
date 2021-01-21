class Heap3:
    def __init__(self):
        self.list = [0]

    def insertItem(self, key):
        assert len(self.list) < 99
        self.list.append(key)
        # 현재 삽입한 노드부터 upHeap 
        self.upHeap(self.list.index(key))

    def upHeap(self, cur_index):
        parent_index = cur_index//2
        if cur_index == 1:
            return 
        # 부모 노드가 삽입한 노드보다 크면 upHeap 중단
        if self.list[parent_index] > self.list[cur_index]:
            return

        cur = self.list[cur_index]
        parent = self.list[parent_index]
        self.list[cur_index], self.list[parent_index] = self.list[parent_index], self.list[cur_index]
        self.upHeap(parent_index)

    def downHeap(self, i, last):
        cur_index = i
        left_index = 2*i
        right_index = 2*i+1

        if last < 2*i:
            return
        bigger = left_index
        if last >= right_index:
            if self.list[bigger] < self.list[right_index]:
                bigger = right_index

        if self.list[cur_index] > self.list[bigger]:
            return
        
        self.list[cur_index], self.list[bigger] = self.list[bigger], self.list[cur_index]
        self.downHeap(bigger, last)

    def inplaceHeapSort(self, keys):
        for key in keys:
            self.insertItem(key)
        for i in range(len(self.list)-1, 1, -1):
            self.list[1], self.list[i] = self.list[i], self.list[1]
            self.downHeap(1, i-1)

    def printHeap(self):
        assert len(self.list) >= 2
        for data in self.list[1:]:
            print(data, end=' ')
        print('')

    def main(self, keys):
        self.inplaceHeapSort(keys)
        self.printHeap()
        return 


H = Heap3()
n = int(input())
keys = [int(i) for i in input().split()]
H.main(keys)