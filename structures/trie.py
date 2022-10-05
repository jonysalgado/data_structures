class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.result_buffer = []
        
    def dfs_with_prefix(self, curr, word):
        if len(self.result_buffer) == 3:
            return
        if curr.is_word:
            self.result_buffer.append(word)
            
        for letter in range(ord('a'), ord('z')+1):
            idx = letter - ord('a')
            if curr.children[idx] is not None:
                self.dfs_with_prefix(curr.children[idx], word + chr(letter))
                
    def insert(self, s):
        
        curr = self.root
        for c in list(s):
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            
        curr.is_word = True
        
    def get_words_starting_with(self, prefix):
        curr = self.root
        self.result_buffer = []
        
        for c in list(prefix):
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return self.result_buffer
            curr = curr.children[idx]
        
        self.dfs_with_prefix(curr, prefix)
        return self.result_buffer