class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def newNode(key):
    return Node(key)

x = Node(5)
x.next = Node(10)
x.next.next = Node(41)
x.next.next.next = Node(87)

y=Node(7)
y.next=Node(14)
y.next.next=Node(30)

l=[]
while (x is not None):
    l.append(x.key)
    x = x.next

while (y is not None):
    l.append(y.key)
    y=y.next

l.sort()
result=Node(-2)
temp=result
for i in range(len(l)):
    result.next=Node(l[i])
    result=result.next
temp=temp.next