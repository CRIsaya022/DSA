# Queue
from collections import deque
class my_queue:
    def __init__(self):
        self.queue = deque()

    # add an item
    def enqueue(self, data):
        self.queue.append(data)
    
    # remove an item
    def dequeue(self):
        return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        return self.queue[0]
    
queue = my_queue()
queue.enqueue("Queue weekdays:")
queue.enqueue("Monday")
queue.enqueue("Tuesday")
queue.enqueue("Wednesday")
queue.enqueue("Thursday")
queue.enqueue("Friday")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

"""
Output:
Queue weekdays:
Monday
Tuesday
Wednesday
Thursday
Friday
"""



    


    