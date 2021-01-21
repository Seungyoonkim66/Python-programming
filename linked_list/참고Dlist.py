class Node:
    def __init__(self, elem, prev, next):
        self.elem = elem
        self.prev = prev
        self.next = next


class DList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, position, elem):
        if((elem.isalpha() == 0) or (position < 1)):
            print("invalid position")
            return
        if position == 1:
            new = Node(elem, self.head, self.head.next)
            self.head.next.prev = new
            self.head.after = new
            self.size += 1
        else:
            target = self.head
            cur = 0
            while cur < position-1:
                target = target.next
                cur += 1
            new = Node(elem, target, target.next)
            target.next.prev = new
            target.next = new
            self.size += 1

    def delete(self, position):
        cur = 0
        target = self.head

        while cur < position:
            target = target.next
            cur += 1

        target.next.prev = target.prev
        target.prev.next = target.next
        self.size -= 1

    def get(self, position):
        cur = 1
        target = self.head.prev

        if ((position > self.size) or (position < 1)):
            print("invalid position")
            return

        while cur < position:
            target = taeget.next
            cur += 1

        print(target.elem)

    def print(self):
        if self.isEmpty():
            print("invalid position")
            return

        temp = self.head.next

        while temp != self.tail:
            print(temp.elem, end='')
            temp = temp.next
        print("")


N = int(input())
list = DList()

for i in range(N):
    temp = input().split()

    if temp[0] == 'A':
        try:
            list.add(int(temp[1]), temp[2])
        except (AttributeError, ValueError):
                print("invalid position")
    elif temp[0] == 'D':
        try:
            list.delete(int(temp[1]))
        except (AttributeError, ValueError):
            print("invalid position")
    elif temp[0] == 'G':
        try:
            list.get(int(temp[1]))
        except (AttributeError, ValueError):
                print("invalid position")
    elif temp[0] == 'P':
        list.print()
    else:
        break
