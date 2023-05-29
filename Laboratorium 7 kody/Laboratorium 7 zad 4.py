class Node:

    def __init__(self, data):
        self.data=data
        self.next=None

class List:

    def __init__(self):
        self.head=None

    def sortedInsert(self, new_node):

        if self.head is None:
            new_node.next=self.head
            self.head=new_node

        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head=new_node

        else:
            current=self.head
            while (current.next is not None and
                   current.next.data<new_node.data):
                current=current.next

            new_node.next=current.next
            current.next=new_node

    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        temp=self.head
        while (temp):
            print(temp.data, temp=temp.next)