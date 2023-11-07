#k-ary search tree used for storing + searching specific key from set
#Search complexities can be brought to optimum limit (key length)
#Used for storing strings over an alphabet and can be used to store large amount of strings


#Every node of Trie has multiple branches
#Each branch represents a possible character of keys
#We need to mark the last node of every key as leaf node
#A Trie node field isEndOfWord is used to distinguish the node as leaf node
#A simple structure to represent nodes of English alphabet can be as following:

# Trie node
class TrieNode:
    #constructor
    def __init__(self):
        self.children = [None]*ALPHABET_SIZE
        #isEndOfWord is True if node represents end of a word
        self.isEndOfWord = False

class Trie:
    #constructor
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        #returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self,ch):
        #private helper function
        #converts key current character into index
        #use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')

    def insert(self,key):
        #if not present, inserts key into trie
        #if the key is prefix of trie node, just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            #if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        #mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self,key):
        #search key in the trie
        #returns true if key presents in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def delete(self,key):
        #delete key from trie
        #returns true if key was deleted successfully, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        if pCrawl != None and pCrawl.isEndOfWord:
            pCrawl.isEndOfWord = False
            return True
        return False