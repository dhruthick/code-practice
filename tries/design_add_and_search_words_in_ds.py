'''
211: MEDIUM
Design a data structure that supports adding new words and 
finding if a string matches any previously added string.

Implement the WordDictionary class:

- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, 
it can be matched later.
- bool search(word) Returns true if there is any 
string in the data structure that matches word or 
alse otherwise. word may contain dots '.' where dots 
can be matched with any letter.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    # Use trie logic
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def backtrack_search(word, node):
            for i, c in enumerate(word):
                if c not in node.children:
                    # check all children if .
                    if c == '.':
                        for child in node.children:
                            if backtrack_search(word[i + 1:], node.children[child]):
                                return True
                    return False
                else:
                    node = node.children[c]
            return node.isEnd
        return backtrack_search(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)