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

def onp(y):
    x=Stack()
    i=0
    while i < len(y):
        symbol=y[i]
        if symbol.isdigit()==True:
            x.push(symbol)

        elif symbol=="+" or symbol=="-" or symbol=="/" or symbol=="*":
            a=str(x.peek())
            x.pop()
            b=str(x.peek())
            x.pop()
            c=eval(b+symbol+a)
            x.push(c)

        elif symbol=="^":
            symbol="**"
            a=str(x.peek())
            x.pop()
            b=str(x.peek())
            x.pop()
            c=eval(b+symbol+a)
            x.push(c)

        elif symbol=="=":
            return x.peek()
        i+=1

print(onp( "7 3 + 5 2 - 2 ^ * =" ))


