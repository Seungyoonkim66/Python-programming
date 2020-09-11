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

    def add(self, pos, data):
        if pos <= 0:
            print("invalid position")

        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            newnode = Node(data)

            # 연결리스트 맨 앞 부분에 삽입하는 경우
            if temp == self.head:
                self.head.next.prev = newnode
                newnode.next = self.head.next
                self.head.next = newnode
                newnode.prev = self.head
            
            # 연결리스트 맨 뒷 부분에 삽입하는 경우
            elif self.tail.prev == temp:
                temp.next.prev = newnode
                newnode.next = temp.next
                temp.next = newnode
                newnode.prev = temp
            
            # 가운데 삽입하는 경우 
            else:
                temp.next.prev = newnode
                newnode.next = temp.next
                temp.next = newnode
                newnode.prev = temp
            
            self.size += 1
    
    def show(self):
        temp = self.head
        for i in range(self.size):
            temp = temp.next
            print("%s" %(temp.data), end="")
        print("")

    def rem(self, pos):
        temp = self.head      
        if pos <= 0 or pos > self.size:
            print("invalid position") 
        else:
            for i in range(pos):
                temp = temp.next
            nextnode = temp.next
            prenode = temp.prev
            prenode.next = nextnode
            nextnode.prev = prenode
            temp.next = None
            temp.prev = None

            self.size -= 1
    
    def get(self, pos):
        temp = self.head      
        if pos <= 0 or pos > self.size:
            print("invalid position") 
        else:
            for i in range(pos):
                temp = temp.next
            print("%s" %(temp.data))



list = DList()
n = int(input())
for i in range(n):
    en = input().split()
    op = en[0]
    if op == 'A':
        pos, data = int(en[1]), en[2]
        list.add(pos, data)
    elif op == 'P':
        list.show()
    elif op == 'D':
        pos = int(en[1])
        list.rem(pos)
    elif op == 'G':
        pos = int(en[1])
        list.get(pos)
