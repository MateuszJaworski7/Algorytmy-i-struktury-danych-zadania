class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


o=["[", "{", "("]
z=["]", "}", ")"]

def funkcja(y):
    x = Stack()
    for i in y:
        if i in o:
            x.push(i)
        elif i in z:
            a = z.index(i)
            if x.size() > 0 and o[a] == x.peek():
                x.pop()
            else:
                return False
    if x.size() == 0:
        return True
    else:
        return False