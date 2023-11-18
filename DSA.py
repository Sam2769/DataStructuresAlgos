class btNode:

    def __init__(self,value):

        self.data = value
        self.left = None
        self.right = None

class Queue:

    def __init__(self):

        self.front = -1
        self.arr = []
        self.__size = 0

    def Size(self):

        return self.__size

    def enqueue(self,item):

        if self.front == -1:
            self.arr.append(item)
            self.front += 1
            self.__size += 1
            return

        self.arr.append(item)


    def isEmpty(self):

        return self.front == -1

    def peek(self):

        return self.arr[self.front]

    def dequeue(self):

        if self.front == -1:
            print("Queue Underflow")
            return -1

        if self.front == len(self.arr):
            print("Queue is Empty")
            return -1

        element = self.arr[self.front]
        self.front += 1
        self.__size -= 1

        return element


    def printQueue(self):

        if self.front == -1 or self.front == len(self.arr):
            print(-1)

        for f in range(self.front, len(self.arr)):

            print(self.arr[f], end = " ")

def takeInput():

        r = int(input("Enter root value\n"))
        root = btNode(r)

        if root.data == -1:
            return None

        leftTree = takeInput()
        rightTree = takeInput()

        root.left = leftTree
        root.right = rightTree


        return root

class BinaryTree:

    def __init__(self,root):

        self.root = root

    def levelOrderTraversal(self,root):

        if root == None:
            return []

        main = []
        q = Queue()


        while not q.isEmpty():

            vList = []

            size = q.Size()
            for f in range(size):
                vList.append(q.peek())
                q.dequeue()

            for i in range(size):

                node = vList[i]
                if node.left is not None:
                    q.enqueue(node.left)

                if node.right is not None:
                    q.enqueue(node.right)

                main.append(vList)


        return main


root = takeInput()
bt = BinaryTree(root)

