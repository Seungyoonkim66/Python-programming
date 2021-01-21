class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        print("insert")
        if self.root is None:
            self.root = key
    
    def delete(self, key):
        pass

    def search(self, key):
        pass

    def printPreorder(self):
        pass

if __name__ == "__main__":
    BST = BinarySearchTree()
    op = 'start'
    while op[0] != 'q':
        op = input()
        if op[0] == 'i':
            key = op[2:]
            BST.insert(key)
        elif op[0] == 'd':
            key = op[2:]
            BST.delete(key)
        elif op[0] == 's':
            key = op[2:]
            BST.search(key)
        elif op[0] == 'p':
            BST.printPreorder()
