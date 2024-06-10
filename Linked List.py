class Node:

    def __init__ (self, data):
        self.data=data
        self.next=None
    
class LinkedList:

    def __init__(self):
        self.head=Node
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printllist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


if __name__ == '__main__':

    llist=LinkedList()

    llist.head=Node(1)

    second=Node(2)
    third=Node(3)

    llist.head.next=second
    second.next=third

    llist.printllist()

    llist.reverse()
    llist.printllist()







