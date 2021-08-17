class MyHashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        self.hashTable = [None] * size
        self.length = 0
        self.hashfunction = hash1
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        #print(key, data)
        arr_index = self.hashfunction(key) #converting key to index
        
        if self.hashTable[arr_index] is None:
            self.hashTable[arr_index] = data
            self.length = self.length + 1
            return True
        else:
            return False
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        try:
            #self.hashTable[key]
            return self.hashTable[key]
        except:
            return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        if self.length == len(self.hashTable):
            return True
        else:
            return False

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        #pass
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        self.length = self.length + 1
        arr_index = self.hashfunction(key) #converting key to index
        node = self.hashTable[arr_index]
        
        try:
            if node is None: # slot is empty -> MyHashTable
                self.hashTable[arr_index] =  Node(arr_index, data) 
                #self.length = self.length + 1
                return True
            elif node is not None:     #interate to end of chain
                chaining = node #start chaining
                while node is not None:
                    chaining = node
                    node = node.chain # last node in linked list
                chaining.chain = Node(key, data)
                return True
        except:
            return False


    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        arr_index = self.hashfunction(key) #converting key to index
        node = self.hashTable[arr_index]

        while node is not None and node.key != key: #iterate thru linked list
            #print('here ---> ', node.key, node.chain, node.chain.data, key)
            node = node.chain  #last available

        if node is None:
            return None
        else:
            #print(node.data, node.key)
            return node.data
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        if self.length == len(self.hashTable):
            return True
        else:
            return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hashfunction2 = hash2
        #pass
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        arr_index1 = self.hashfunction(key)
        arr_index2 = self.hashfunction2(key)
        
        if self.hashTable[arr_index1] is None: # slot is empty
            #print('first block')
            self.hashTable[arr_index1] = data
            self.length = self.length + 1
            return True
        elif self.hashTable[arr_index1] is not None: # slot is not empty
            #print('in here', arr_index2)
            #print(arr_index2)
            try:
                i = 1
                while i < len(self.hashTable):
                    val = (arr_index1 + i*arr_index2) % len(self.hashTable) # getting new index
                    if self.hashTable[val] is None: # no collision -> store new key
                        self.hashTable[val] = data
                        self.length = self.length + 1
                        return True
                        break  # avoid infinite loop
                    i = i + 1
                #print(i)
            except:
                return False     
        else:
            #print('here - else')
            pass
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        try:
            #self.hashTable[key]
            return self.hashTable[key]
        except:
            return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.length


class Node:
    def __init__(self, key, data, node=None):
        # Initialize this node, insert data, and set the next node if any
        self.key=key
        self.data=data
        self.chain=node
