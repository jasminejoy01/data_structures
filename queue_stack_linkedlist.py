class MyQueue:
    def __init__(self,data=None):
        self.head = data
        self.tail = None
        self.length = 0
    
    def peek(self):
        if self.head is None or self.tail is None:
            print("Queue is empty")
            self.length = 0
            return self.head, self.tail
        return self.head.data, self.tail.data
    
    def enqueue(self,data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            #self.head.next = data
            self.tail = self.head
            #print(self.peek(), "tail is None")
        else:
            self.tail.next = new_data
            self.tail = self.tail.next
            #print(self.peek(), "tail not None")
        self.length = self.length + 1
        return data

    def dequeue(self):
        data = self.head.data
        #print(self.peek(), data)
        self.head = self.head.next
        if self.head is None:
            self.tail is None
        self.length = self.length - 1
        #print(data)
        return data
    
    def __len__(self):
        return (self.length)

class MyStack:
    def __init__(self, data=None):
        self.top = None
        self.length = 0
    
    def push(self, data):
        new_data = Node(data)
        if self.top is None: #empty
            self.top = new_data
        else:
            new_data.next = self.top
            self.top = new_data
        self.length = self.length + 1
        
    def pop(self):
        if self.top is not None:
           data = self.top.data
           self.top = self.top.next
           self.length = self.length - 1
           return data
        else:
           return None
            
    def __len__(self):
        return (self.length)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

# obj = MyQueue(100)

# print(obj.head)
# a =MyQueue(100)

# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.enqueue(5)

# obj.dequeue()
# obj.dequeue()
# obj.dequeue()
# obj.dequeue()
# print(obj.dequeue())
