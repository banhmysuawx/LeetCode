from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def list_print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def atBegin(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        
    def atEnd(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2
e2.next = e3

list.atBegin("Sun")
list.atEnd("Sat")
list.list_print()