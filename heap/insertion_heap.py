class MaxHeap(object):
    def __init__(self):
        self.list = [0] # 0번 인덱스 사용 X

    def heapify(self, i):
        left_index = i*2+1
        rigth_index = i*2+2
        max_index = i

        if left_index <= len(self.list)-2 and self.list[max_index] < self.list[left_index]:
            max_index = left_index
        if rigth_index <= len(self.list)-2 and self.list[max_index] < self.list[left_index]:
            max_index = rigth_index
        if max_index != i:
            self.list[i], self.list[max_index] = self.list[max_index], self.list[i]
            self.heapify(max_index)
    
    def upheap(self, i):
        parent_index = (i-1)//2
        while i > 1 and self.list[parent_index] < self.list[i]:
            self.list[i], self.list[parent_index] = self.list[parent_index], self.list[i]
            i = parent_index

    def insert(self, n):
        self.list.append(n)
        last_index = len(self.list)-1 #n의 위치 
        self.upheap(last_index)
        # while 1 <= last_index:
        #     parent_index = (last_index-1)//2
        #     if (1 <= parent_index) and (self.list[parent_index] < self.list[last_index]):
        #         self.list[last_index], self.list[parent_index] = self.list[parent_index], self.list[last_index]
        #         last_index = parent_index
        #     else: 
        #         break

    def delete(self):
        delete_key = self.list[1]
        self.list.remove(delete_key)
        self.heapify(1)
        return delete_key

    def Hprint(self):
        return self.list

mx = MaxHeap()
op = ""
res = []
while op != "q":
    op = input("").split(" ")
    if op[0] == "i":
        n = int(op[1])
        mx.insert(n)
        res.append(0)
    elif op[0] == "d":
        res.append(mx.delete())
    elif op[0] == "p":
        p = []
        i = 1
        list = mx.Hprint()
        while i <= len(list)-1:
            p.append(list[i])
            i += 1
        res.append(p)
    elif op[0] == "q":
        break

for i in res:
    if (str(type(i))) == "<class 'list'>":
        for j in i:
            print(" %d" %(j), end="")
        print("")
    else:
        print(i)


