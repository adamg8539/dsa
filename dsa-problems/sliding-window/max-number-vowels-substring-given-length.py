def maxVowels(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    isVowelArray = []
    for x in s:
        if x in ['a', 'e', 'i', 'o', 'u']:
            isVowelArray.append(True)
        else:
            isVowelArray.append(False)
        
    vowelCounter = 0
    x = 0
    while x < k:
        if isVowelArray[x]:
            vowelCounter += 1
        x += 1
    
    maxVowelCounter = vowelCounter
    while x < len(s):
        if isVowelArray[x]:
            vowelCounter += 1
        if isVowelArray[x-k]:
            vowelCounter -= 1
        
        if vowelCounter > maxVowelCounter:
            maxVowelCounter = vowelCounter
        
        x += 1
    
    return maxVowelCounter