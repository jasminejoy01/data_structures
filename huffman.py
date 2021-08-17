import heapq
        
var1 = ''
class MyHuffman():
    def __init__(self):
        # Initialize the Huffman tree      
        #dictionay to hold the characters and their coressponding bitcode
        self.chars = {}
        #Huffman tree
        self.tree = None
        self.nodes = {}      
        # position in the bitstring being decoded
        self.decodePosition = 0
          
    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        #priority nodes
        prioq = []
        for i in weights:  
             #val = (i, weights[i])
             #print(val, val[-1])
             prioq.append(Node(i, weights[i]))
        heapq.heapify(prioq)

        s_result = [heapq.heappop(prioq) for i in range(len(prioq))]
        self.nodes = s_result
        # #print(s_result[0].value)
        
        if len(s_result) == 1:
            return
        else:
            while len(s_result) > 1:
                 n1 = heapq.heappop(s_result) #smallest value popped and returned
                 n2 = heapq.heappop(s_result) #smallest value popped and returned
                 n3 = Node("#",n1.data + n2.data)
                 n3.left = n1
                 n3.right = n2
                 heapq.heappush(s_result, n3)
        # result dwindles to one tree saved in s_result.
        self.tree = s_result[0]       
                       
    def makeLookupTable(self, node, bitCode=''):
        if node is not None:
            self.makeLookupTable(node.left, bitCode + '1')
            self.makeLookupTable(node.right, bitCode + '0')
            self.chars[node.value] = bitCode

        
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        self.makeLookupTable(self.tree, '') # traverse tree to find bitstring for each node
        encode_word = ""
        for i in word:
            encode_word = encode_word + self.chars[i]
        #print(encode_word)
        return encode_word
            
    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        #print(self.chars)
        #print(bitstring)
        code = ""
        decode_word = ""
        for bit in bitstring:
            if bitstring != '':
                val = self.recursiveTraverseTree(self.tree, bitstring)
                decode_word = decode_word + val[0]
                code = val[-1]
                bitstring = code
        #print(decode_word)
        return decode_word
    
    def recursiveTraverseTree(self, node, bitString=''):
        # Return the character after traversing the Huffman tree through the bitstring
        #print(bitString)
        for i in bitString:
            if (i == '1'):
                node = node.left
                #print('left', i, node.data, node.value)
                self.decodePosition = self.decodePosition + 1
                self.recursiveTraverseTree(node)
            elif (i == '0'):
                node = node.right
                #print('right',i, node.data, node.value)
                self.decodePosition = self.decodePosition + 1
                self.recursiveTraverseTree(node)
        
            if node.value == '#':
                pass
            else:
                #print('out of loop',node.data, node.value, self.decodePosition, bitString , bitString[self.decodePosition:] )
                newBitString = bitString[self.decodePosition:]
                self.decodePosition = 0
                return (node.value, newBitString)
        
# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        self.left = None
        self.right = None
        self.data = data #data stored in each node
        self.value = value #character stored in each node

    def __lt__(self, other):
        return self.data < other.data
    
    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data
    
    def __ge__(self, other):
        return self.data >= other.data
