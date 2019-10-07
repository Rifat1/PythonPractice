class BinaryTree(object):
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
r=BinaryTree('a')
# print(r.getRootVal())   
r.insertLeft('b')
r.insertRight('c')

# print(r.getLeftChild().getRootVal())

def preOrder(tree):
    if tree:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())
# preOrder(r)
def inOrder(tree):
    if tree:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())
# inOrder(r)      
def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())
postOrder(r)

