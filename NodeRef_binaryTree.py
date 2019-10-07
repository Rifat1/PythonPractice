class BinaryTree(object):
    
    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):

        if self.leftChild== None:
            self.leftChild=BinaryTree(newNode)

        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):

        if self.rightChild== None:
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
        self.Key=obj

    def getRootVal(self):
        return self.key



def printInorder(root):
    if root:
        printInorder(root.getLeftChild())
        print(root.getRootVal())
        printInorder(root.getRightChild())

def printPostorder(root):
    if root:
        printPostorder(root.getLeftChild())
        printPostorder(root.getRightChild())
        print(root.getRootVal())

def printPreorder(root):
    if root:
        print(root.getRootVal())
        printPreorder(root.getLeftChild())
        printPreorder(root.getRightChild())





def main():
    r=BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    
    
    r.insertLeft('b')
    print(r.getLeftChild().getRootVal())
main()


