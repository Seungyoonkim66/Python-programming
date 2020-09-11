class Node:
    def __init__(self, data):
        self.data = data
        self. prev = None
        self. next = None

class DList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.next = None
        self.head.prev = self.head
        self.size = 0


    

list = DList()

N = int(input())
i = 0
while i < N:
    op, pos, data = input().split()
    pos = int(pos)
    newnode = Node(data)
    if op == 'A':
        list.add(pos, newnode)
    # elif op == 'D':
    #     List.del(pos)
    # elif op == 'G':
    #     print(get(temp.data))
    # elif op == 'P':
    #     print()