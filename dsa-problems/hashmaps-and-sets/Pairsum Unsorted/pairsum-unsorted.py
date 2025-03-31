from typing import List

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsDict = {}
    for w, x in enumerate(nums):
        if x in numsDict:
            numsDict[x].append(w)
        else:
            numsDict[x] = [w]

    for x in nums:
        newT = target-x
        if newT == x:
            if len(numsDict[x]) > 1:
                return [numsDict[x][0],numsDict[x][1]]
            continue
        if newT in numsDict:
            return [numsDict[x][0], numsDict[newT][0]]

    return []