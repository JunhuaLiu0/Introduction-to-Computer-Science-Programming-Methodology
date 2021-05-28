class Node:
    def __init__(self,element,pointer):
        self.element=element
        self.pointer=pointer

class SinglyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def insert(self,data):
        newest=Node(data,None)
        newest.pointer=self.head
        self.head=newest
        self.size+=1
        if self.size==1:
            self.tail=newest

    def recursive_count(self,node):
        if (isinstance(node, Node) == False) or (node == None):
            return 0
        else:
            return 1 + self.recursive_count(node.pointer)

a = SinglyLinkedlist()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
print("The number of node is:", a.recursive_count(a.head))
