class MyQueue:
    def __init__(self, data=None, maxSize = 100000):
        # Initialize this queue, and store data if it exists
        self.data = data
        self.head = 0
        self.tail = 0
        self.size = maxSize
        self.queue = [None]*self.size
        if data != None:
            self.enqueue(data)

    def enqueue(self, data):
        #print(self.maxSize, data, self.size, self.tail)
        if self.tail == self.size:
            return("Queue is full!")
        else:
            self.queue[self.tail] = data
            #self.size = self.size + 1
            self.tail = self.tail + 1
            #self.tail = (self.tail+1) % self.maxSize
            
    def dequeue(self):
        if self.tail < 1:
            return("Empty Queue")
        else:
            val = self.queue[self.head]
            #print("headval", self.head, val)
            self.head = (self.head+1) % len(self.queue)
            self.tail = self.tail - 1
            #print(val, self.tail)
            return val

    def __len__(self):
        return self.tail

class MyStack:
    def __init__(self, data=None, maxSize = 100000):
        self.data = data    
        self.top = 0
        self.size = maxSize
        self.stack = [None]*self.size
        if data != None:
            self.push(data)
    
    def push(self, data):
        #print(self.top, self.stack, data)
        if self.top == self.size:
            pass
        else:
            self.stack[self.top] = data
            self.top = self.top + 1 
            #print(data, self.top, self.stack[self.top], self.stack )

    def pop(self):
        if self.top < 1:
            return None
        else:
            #print(self.top, self.stack[self.top-1], self.stack)
            self.top = self.top - 1
            val = self.stack[self.top]
            self.stack[self.top] = None
            #print(val)
            return val

    def __len__(self):
        return self.top

# q = MyQueue()
# q.enqueue(1)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()