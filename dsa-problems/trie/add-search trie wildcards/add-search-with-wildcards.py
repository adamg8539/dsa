class TrieNode:
    def __init__(self):
        self.charMap = {}
        self.end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
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
        def dfs(currRoot, c):
            curr = currRoot
            for x in range(c, len(word)):
                if word[x] in curr.charMap:
                    curr = curr.charMap[word[x]]
                elif word[x] == ".":
                    for b in curr.charMap.keys():
                        if dfs(curr.charMap[b], x + 1):
                            return True
                    return False
                else:
                    return False
            return curr.end
        return dfs(self.root, 0)