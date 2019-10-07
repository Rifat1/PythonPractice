class Node:
  """Lightweight, nonpublic class for storing a singly linked node."""
  __slots__ = 'element', 'next'       # streamline memory usage

  def __init__(self, element, next):  # initialize node's fields
    self.element = element            # reference to user's element
    self.next = next 

class IntBag:
    def __init__(self):
        self.head=None
        self.bag=Node(None,None)

    def addItem(self,Item):
        if head==None:   
            head=Node(Item,None)
        else:
            head=Node(Item,head)
   
bag1=IntBag()

bag1.addItem("pens")
bag1.addItem("phone")
bag1.addItem("laptop")

print(bag1.head)
