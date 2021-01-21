class Heap3:
    def __init__(self):
        self.list = [0, None]

    def insert(self,i):
        

    def print(self):
        for i in self.list[1:]:
            print(i, end=" ")
        print()

h = Heap3()
n = int(input())
keys = input().split()
for i in keys:
    h.insert(i)
h.print()