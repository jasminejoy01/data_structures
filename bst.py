contain = 0

class MyBST:
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        self.parent = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = 0
        #self.nodes = []

    def insert(self, data, count = 0):
        global contain
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        #self.nodes.append(data)
        if data < self.data:
            if self.left is None:
                self.left = MyBST(data)
                #print(" <<<< Inserted Tree Left of", self.data, " with node", data)
            else:
                self.left.insert(data, count + 1)
        elif data >= self.data:
            if self.right is None:
                self.right = MyBST(data)
                #print(" >>>> Inserted Tree right of", self.data , " with node" , data)
            else:
                self.right.insert(data, count + 1)
                
        if contain <= count : 
            contain = count
            
        self.height = contain + 1

        return self
            
    def __contains__(self, data):
        #print(self.parent)
        if data is not None:
            if data == self.data:
                #print(self.data, data)
                return True
            elif data == self.parent and data not in self.left and data not in self.right:
                print(data, self.parent)
                return False
            elif self.left is not None and data in self.left:
                #print(self.left.data, data in self.left)
                return True
            elif self.right is not None and data in self.right:
                #print(self.right.data, data in self.right)
                return True
            else:
                return False
     
    def getHeight(self):
        return self.height

# n = 7
# m = 20

# bst= MyBST(n)
# import random 


# try:
#     bst = MyBST(n)
# except:
#     print("Error: MyBST not creatable")


# try:
#     bst=bst.insert(n+1)
# except:
#     print("Error: BST not insertable")


# try:
#     bst=bst.insert(n-1)
# except:
#     print("Error: BST not insertable")


# if bst.getHeight() != 1: # or bst.getHeight() != CheckHeight(bst):
#     print("Error: BST height incorrect")


# try:
#     bst=bst.insert(n+2)
#     bst=bst.insert(n+3)
# except:
#     print("Error: BST not insertable")


# if bst.getHeight() != 3: # or bst.getHeight() != CheckHeight(bst):
#     print("Error: BST height incorrect.")




# del(bst)
# bst= MyBST(n)

# a = []
# for i in range(1000):
#     v = random.randint(0,m)
#     bst= bst.insert(v)
#     if not(v in a):
#         a.append(v)
    
# for i in range(1000):
#     if len(a) >= 10:
#         m*=2
#     v = random.randint(0,m)
#     if (v in a) != (v in bst):
#         #print(v in a, v in bst)
#         #print(a, v, v in a, v in bst)#, bst.nodes)
#         print("Error: BST Search incorrect")



# del(bst)









