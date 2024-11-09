# Stack
class my_stack:
    # initialize a stack
    def __init__(self):
        self.stack = []
    # add an element
    def push(self, data):
        self.stack.append(data)

    # remove an element
    def pop(self):
        return self.stack.pop()
    
    # check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # check top element
    def peek(self):
        return self.stack[-1]
    
stack = my_stack()
stack.push("morning")
stack.push("afternoon")
stack.push("evening")
stack.push("Pop times from the last:")

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

"""
Output:
Pop times from the last:
evening
afternoon
morning
"""    
