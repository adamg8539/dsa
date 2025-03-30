def next_lexicographical_sequence(s: str) -> str:
    # Write your code here
    pass
    intList = strToNum(s)
    listLen = len(intList)-1
    finalList = []
    if (listAsc(intList)):
        a = listLen
        while (a > 0):
            if intList[a] > intList[a-1]:
                temp = intList[a]
                intList[a] = intList[a-1]
                intList[a-1] = temp
                break
            a -= 1
        return ''.join(chr(x) for x in intList)
    for x in range (listLen):
        if (intList[x] > intList[x+1]):
            workList = intList[x:]
            if (x-1 < 0):
                workList = intList
            if(listDesc(workList)):
                workList.sort()
                if x == 0:
                    finalList = workList
                    break
                for z,y in enumerate(workList):
                    if y > intList[x-1]:
                        temp = intList[x-1]
                        intList[x-1] = y
                        workList[z] = temp
                        finalList = intList[:x] + workList
                        break
            else:
                if (intList[x+1] > intList[x+2]):
                    continue
                workList = intList[x+2:]
                workList.sort()
                for z, y in enumerate(workList):
                    if y > intList[x+1]:
                        temp = intList[x+1]
                        intList[x+1] = y
                        workList[z] = temp
                        finalList = intList[:x+2] + workList
                        break
                break
    return ''.join(chr(x) for x in finalList)



def listDesc(l: list) -> bool:
    return all(earlier >= later for earlier, later in zip(l, l[1:]))

def listAsc(l: list) -> bool:
    return all(earlier <= later for earlier, later in zip(l, l[1:]))

def strToNum(s: str) -> list:
    strList = list(s)
    intList = []
    for x in strList:
        intList.append(ord(x))
    return intList

def listToStr(l: list) -> str:
    return ''.join(chr(x) for x in l)