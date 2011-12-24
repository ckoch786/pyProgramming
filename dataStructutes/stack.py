# An implementation of the stack adt
# def stackInterface():
#   """A stack is  a FIFO data structute"""
#
#
#    #removes item from the top of the stack
#    # throws a stack underflow exception if stack is empty
#    pop()
#
#    #returns item from the top of the stack
#    # throws a stack underflow exception if stack is empty
#    top()
#
#    # adds item to the bottom of the stack
#    push()
#
#    # Returns true is stack is empty else returns false
#    isEmpty()

class Stack:
    Name = "stack"
    # __init__ is a class constructor
    # __***__ is usually a special class method.
        
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return (self.items == [])




def main():
    s = Stack()
    x = "Hello"
    s.push(x)
    item = s.pop()
    print item


if __name__ == '__main__':
    main()


