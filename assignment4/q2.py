class Node:
    def __init__(self, element):
        self.element = element
        self.pointer = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.tail.pointer = self.tail = Node(data) 
        self.size += 1

    def printList(self):
        tmp = self.head
        print("\nSorted:")
        while tmp != None:
            print("Element:",tmp.element,"\t",end="")
            print("Pointer:",tmp.pointer)
            tmp = tmp.pointer
        print("\nreturn of head node:","\nElement:",self.head.element,end="")
        print("\tPointer:",self.head.pointer)

    def raw_printList(self):
        tmp = self.head
        print("Raw:")
        while tmp != None:
            print("Element:",tmp.element,"\t",end="")
            print("Pointer:",tmp.pointer)
            tmp = tmp.pointer\

    def swap(self, x, y):
        x.element, y.element = y.element, x.element

    def partition(self, left, right):
        x = left.element
        i = left
        j = left.pointer
        while j != right:
            if j.element <= x:
                i = i.pointer
                self.swap(i, j)
            j = j.pointer
        self.swap(i, left)
        return i

    def sort(self, left, right):
        if left != right:
            p = self.partition(left, right)
            self.sort(left, p)
            self.sort(p.pointer, right)

    def quick_sort(self,node):
        self.sort(node.head, None)

a = SinglyLinkedList()
a.insert(5)
a.insert(4)
a.insert(3)
a.insert(1)
a.insert(9)
a.insert(7)
a.raw_printList()
a.quick_sort(a)
a.printList()

