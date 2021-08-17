class MyNode:
    def __init__(self, character):
        # Initialize the trie node as needed
        self.character = character
        self.children = {} 
        self.isTerminal = False

class MyTrie:
    def __init__(self):
        # Initialize the trie node as needed
        self.root = MyNode("*")
        self.children = {}
        self.children_count = 0
        self.word = None
        self.temp_list = []
        self.autocomplete_list = []
    
    def insert(self, word):
        # Insert a word into this trie node
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = MyNode(letter) #create child node if does not exist
            else:
                pass
            current = current.children[letter] #move to the child node
        current.isTerminal = True


    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        # A terminal node will return true if the word passed is ""
        if word == "":
            return True
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            else:
                pass
            current = current.children[letter]
        return current.isTerminal 

    def isTerminal(self):
        # Return true if this node is the terminal point of a word
        if self.children is None:
            return True
        else:
            return False

    def postOrder(self, node, prefix='', position = 0):
        #print(prefix)
        
        if node.isTerminal is True:
            self.temp_list.append(prefix+ node.character)
            #arraytemp.append(prefix+ node.character)
            #self.temp_list.append(prefix )
        
        for each in node.children.values():
            if len(prefix) == position:
                prefix = prefix[:-1]
            self.postOrder(each,prefix+ node.character)
        
        return

    def autoComplete(self, prefix, position=0):
        # Return every word that extends this prefix in alphabetical order
        current = self.root
        #print(len(prefix))
        
        if prefix != "" :
            for letter in prefix:
                if letter not in current.children:
                    return []
                else:
                    current = current.children[letter]
                    currentNode = current
            try:
                self.postOrder(currentNode, prefix, len(prefix))
            except:
                return []
            
            for each in self.temp_list:
                if self.exists(each) is True:
                    self.autocomplete_list.append(each)
    
            self.autocomplete_list = sorted(self.autocomplete_list)
            #print('prefix',prefix)
            return self.autocomplete_list
        else:
            try:
                for each in current.children.values():
                    self.postOrder(each)
            except:
                return []
            
            #self.autocomplete_list = []
            for each in self.temp_list:
                #print(each, self.exists(each))
                if self.exists(each) is True:
                    self.autocomplete_list.append(each)
            #print(self.autocomplete_list)
            self.autocomplete_list = sorted(self.autocomplete_list)
            return self.autocomplete_list

    def traverse(self, node):
        if node.isTerminal is True:
            self.children_count = self.children_count + 1

        for each in node.children.values():
            self.traverse(each)

    def __len__(self):
        # Return the number of words that either terminate at this node or descend from this node
        # A terminal leaf should have length 1, the node A with terminal child leaves B|C should have length 2
        current = self.root
        try:
            self.traverse(current)
        except:
            return 0
        #print(self.children_count)
        return self.children_count

# trie = MyTrie()
# # # words= ["statue's", "preview's", "runnel's", 'crosser', "rebel's", 'trots', "Granada's", 'moussing', 'encoring', 'jackknifes', 'polled', 'harelip', 'brainless', 'displayed', "childlessness's", "Swazi's", 'despoiling', 'coriander', "skivvy's", "prosody's", 'taunt', 'blowsiest', 'earthlings', 'transpositions', "slang's", 'spool', 'Barnabas', "accentuation's", 'appendectomies', 'beaker', 'dislocates', "presto's", 'provocative', "salt's", 'stubborner', 'invisibility', 'fallacy', 'taring', "Cliburn's", "hype's", 'identically', 'moodily', 'miscalling', 'prairie', 'primaries', 'realign', "Peckinpah's", 'computers', 'manumitted', "everglade's", 'portholes', "barometer's", 'suet', 'sonorous', 'showcases', 'showplace', 'ninja', "telemeter's", 'velocity', 'filmier', 'Toyota', 'anew', 'palpitates', 'cranes', "McQueen's", 'utterances', 'rapped', 'tuckers', "routine's", 'lets', 'maizes', 'attiring', 'devised', "Rochelle's", 'ingest', 'prestige', "ear's", 'unspoiled', 'deescalated', 'Fragonard', 'contemporary', "Newfoundland's", 'renegotiate', 'Liberian', "March's", 'provident', 'antidepressant', "Belshazzar's", 'notation', 'slipperier', 'spoofs', 'astronauts', 'vowel', 'schoolgirls', "shipbuilder's", 'functionaries', 'suspected', 'diminish', "Meighen's", 'unmade', 'lectured', "pantaloons's", 'permitting', 'sopranos', 'Susie', 'mulishness', 'scrimped', 'heliotrope', 'literacy', 'internalized', "legman's", 'trident', 'Adams', 'animism', 'staggered', "whittler's", 'Buchenwald', 'righteously', 'unschooled', "Erebus's", "Michelob's", "Arabia's", "dig's", 'illumine', 'scuttling', "walkout's", 'Riefenstahl', 'Scandinavians', 'Percy', 'bakes', 'antiquing', 'playacts', 'clanked', "moleskin's", 'frisking', "profession's", 'sculptured', "Scotchman's", 'impede', 'centralized', 'theatrically', "Saracen's", "motherfucker's", 'fingertips', 'pings', 'vehement', 'do', 'unhand', 'laborer', "Lorenzo's", 'convocation', 'afterburner', "wren's", 'Schelling', "scuttle's", "Honda's", 'incapacitate', 'brassiest', "Popper's", 'dominoes', "dryad's", 'butteriest', 'dangle', 'glare', "musculature's", 'Jacksonville', 'bordered', 'leveling', 'hunches', 'rumble', "oxymoron's", 'gonorrhoea', 'articulation', "sachem's", "uvular's", "Czechoslovakia's", 'homework', 'telegraphing', "cerebellum's", "cooky's", 'finishing', 'recurrence', 'abase', 'Yanks', 'measliest', "dismemberment's", 'onlookers', "Pentecost's", 'clockworks', 'unopened', 'juices', "amaze's", 'ruminants', 'tiaras', 'savaged', "hairline's", 'opossums', 'circle', 'digestion', 'homonyms', 'marihuana', "nobleman's", 'colonizers', 'romping', "straddle's", 'apes', "obloquy's", 'collisions', "gaggle's", 'simpatico', "Susanne's", 'randomly', "Marmara's", "eggplant's", 'unbent', 'returns', 'transgressor', 'sidewise', 'Loews', 'Bjork', 'busses', 'spanning', 'drill', "evidence's"]
# # # # # #words = ["wait", "waiter", "shop", "shopper"]
# # # # # words = ['37777','32004', '37040', '37101', '37701', '37779', '40961', '86904', '37777']
# # #import random
# wordlist = []
# if not wordlist:
#     f = open("american-english-no-accents.txt", "r")
#     readwords = f.readlines()
#     for word in readwords:
#         wordlist.append(word)
# for word in wordlist:
#     trie.insert(word)

# print(trie.__len__())
# print(trie.exists("runnel's")) #True
# print(trie.autoComplete("fasdfasdfasdfasfawef")) 

# # # print(trie.autoComplete("sta"))
# # (trie.autoComplete(""))
# print(trie.autoComplete("ora")) 