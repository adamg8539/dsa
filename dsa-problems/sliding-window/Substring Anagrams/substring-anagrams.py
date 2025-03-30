def substring_anagrams(s: str, t: str) -> int:
    # Write your code here.
    pass
    tList = list(t)
    tLen = len(tList)
    if tLen == 0:
        return 0
    sList = list(s)
    sLen = len(sList)
    if len(sList) == 0:
        return 0
    if tLen > sLen:
        return 0
    anagramMap = {}
    for a in tList:
        if a in anagramMap:
            anagramMap[a] += 1
        else:
            anagramMap[a] = 1
    
    
    checkMap = {}
    for a in range (0, tLen):
        if sList[a] in checkMap:
            checkMap[sList[a]] += 1
        else:
            checkMap[sList[a]] = 1
    count = 0
    if checkMap == anagramMap:
        count += 1
    for a in range(tLen, sLen):
        if sList[a-tLen] in checkMap:
            if checkMap[sList[a-tLen]] == 1:
                checkMap.pop(sList[a-tLen])
            else:
                checkMap[sList[a-tLen]] -= 1
        if sList[a] in checkMap:
            checkMap[sList[a]] += 1
        else:
            checkMap[sList[a]] = 1
        if checkMap == anagramMap:
            count += 1
    
    return count
