class Heap:
    def __init__(self):
        self.list = [0,None]
    
    def insertItem(self,data):
        assert len(self.list) < 100
        # 빈리스트에 insert하는 경우
        if self.list[1] ==None:
            # none을 data로 교체 
            self.list[1] = data
        else:
            self.list.append(data)
        
        # list 마지막 요소 = 현재 삽입한 값 = cur
        cur = self.list[-1]
        self.upHeap(cur)
        return 0


    # upheap 대상이 되는 노드 cur
    def upHeap(self, cur):
        # cur이 root면 그냥 종료 (list에 하나 뿐일 경우)
        if cur == self.list[1]:
            return
        
        # 현재 삽입된 노드의 인덱스 cur_index에 저장 
        cur_index = self.list.index(cur)
        parent_index = cur_index//2

        # 현재 노드가 부모 노드보다 작을 때까지 upHeap 재귀 호출
        if cur < self.list[parent_index]:
            return

        # 현재 노드가 부모 노드보다 크면 부모노드와 swapping
        self.list[cur_index] = self.list[parent_index]
        self.list[parent_index] = cur

        # swap되어 부모 노드 위치로 간 cur node를 다시 upheap 
        self.upHeap(self.list[parent_index])


    def removeMax(self):

        # max heap에서 max는 root이므로 root를 제거하는 것 
        root = self.list[1]
        # list에 요소가 root 하나밖에 없는 경우 remove하면 초기화
        if len(self.list) == 2:
            self.list = [0,None]
            return root 

        temp = self.list[-1]
        # root 지우기
        self.list.remove(root)
        self.list.remove(0)

        self.list.remove(temp)
        # 마지막 노드를 root로 가져와 downHeap 하기 
        self.list = [0,temp] + self.list
        # 제거 후 root 부터 downheap 
        self.downHeap(self.list[1])

        # 출력을 위해 제거된 root return 
        return root 

    def downHeap(self, cur):
        assert cur in self.list

        # downHeap 시작 위치 
        cur_index = self.list.index(cur)
        left_child_index = cur_index*2
        right_child_index = cur_index*2+1

        # cur 노드의 자식 노드가 없는 경우 재귀 종료 
        if (len(self.list) <= left_child_index) & (len(self.list)<=right_child_index):
            return 

        bigger = self.list[left_child_index]
        if(len(self.list) > right_child_index):
            # 오른쪽 자식 노드 > 왼쪽 자식 노드(bigger) -> bigger = right
            if self.list[right_child_index] > bigger:
                bigger = self.list[right_child_index]

            # 자식 노드 중 큰 값보다 현재 노드가 큰 경우 그대로 
            if cur > bigger:
                return

            # 그렇지 않은 경우 bigger 노드와 cur 노드 swap
            bigger_index = self.list.index(bigger)

            self.list[cur_index] = self.list[bigger_index]
            self.list[bigger_index] = cur
            self.downHeap(self.list[bigger_index])

    def printData(self):
        print(end=' ')
        for data in self.list[1:]:
            print(data, end=' ')
        print()

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
