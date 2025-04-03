class TrieNode:
    def __init__(self):
        self.charMap = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word:
            return
        wordList = list(word)
        curr = self.root
        x = 0
        while x < len(wordList):
            if wordList[x] in curr.charMap:
                curr = curr.charMap[wordList[x]]            
            else:
                while x < len(wordList):
                    curr.charMap[wordList[x]] = TrieNode()
                    curr = curr.charMap[wordList[x]]
                    x += 1
                break
            x += 1
        curr.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        wordList = list(word)
        curr = self.root
        for x in wordList:
            if x in curr.charMap:
                curr = curr.charMap[x]
            else:
                return False
        return curr.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        prefixList = list(prefix)
        curr = self.root
        for x in prefixList:
            if x in curr.charMap:
                curr = curr.charMap[x]
            else:
                return False
        return True
