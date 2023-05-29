import random

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


def Ziemniak(x, y):
    q=Queue()
    for nazwa in x:
        q.enqueue(nazwa)

    while q.size()>1:
        for i in range(y):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

a=random.randint(3,20)
print(Ziemniak(["a","b","c","d","e","f"],a))