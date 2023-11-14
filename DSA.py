class btNode:

    def __init__(self,value):

        self.data = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self,root):

        self.root = root


    def preOrderTraversal(self,root):

        if root == None:
            return root

        print(root.data, end = " ")

        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


    def inOrderTraversal(self,root):

        if root == None:
            return root

        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self,root):

        if root == None:
            return root

        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)

        print(root.data)



node = btNode(8)
node2  = btNode(7)
node3 = btNode(6)
node4 = btNode(5)
node5 = btNode(4)
node6 = btNode(3)
node7 = btNode(2)

node.left = node2
node.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

Tree = BinaryTree(node)

Tree.postOrderTraversal(node)