def longest_substring_with_unique_chars(s: str) -> int:
   # Write your code here
    pass
    sList = list(s)
    sLen = len(sList)
    if sList == 0:
        return 0
    count = 0
    sMap = {}
    loopCount = 0
    y = 0
    for x in range(sLen):
        if sList[x] in sMap:
            if loopCount > count:
                count = loopCount
            while sList[y] != sList[x]:
                sMap.pop(sList[y])
                loopCount -= 1
                y += 1
        else:
            sMap[sList[x]] = 0
            loopCount += 1
            if loopCount > count:
                count = loopCount
    return count