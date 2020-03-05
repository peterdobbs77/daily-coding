
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertLeft(ldata):
        self.left = ldata

    def insertRight(rdata):
        self.right = rdata

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def reconstructBinSearchTree(preorder, inorder):

    height = len(preorder) >> 1                 # good ole right-shift
    print('tree height is: {}'.format(height))

    root = Node(preorder[0])
    node = root
    i = 1
    while(True):
        node.left = preorder[i]
        if(preorder[i] == inorder[0]):
            if(preorder[i-1] == inorder[1]):
                break
        i += 1
        node = node.left
    node.right = inorder[2]


preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
reconstructBinSearchTree(preorder, inorder)
