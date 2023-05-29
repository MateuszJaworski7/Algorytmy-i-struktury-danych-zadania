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

def funkcja(y):
    x=Stack()
    i=0
    balanced=True
    while i<len(y) and balanced:
        symbol=y[i]
        if symbol == "(":
            x.push(symbol)
        else:
            if x.isEmpty():
                balanced=False
            else:
                x.pop()
        i+=1
    if balanced and x.isEmpty():
        return True
    else:
        return False

print(funkcja("(()()()())"))
print(funkcja("(((())))"))
print(funkcja("(()((())()))"))
print(funkcja("((((((())"))
print(funkcja("()))"))
print(funkcja("(()()(()"))