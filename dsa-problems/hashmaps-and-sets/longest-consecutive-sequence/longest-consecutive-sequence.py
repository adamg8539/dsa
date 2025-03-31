def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsSet = set(nums)
    longestChain = 0
    for x in nums:
        count = 1
        if (x not in numsSet):
            continue
        numsSet.remove(x)
        # check consecutively bigger nums
        currentNum = x+1
        while (currentNum in numsSet):
            numsSet.remove(currentNum)
            currentNum += 1
            count += 1
        
        #check consecutively smaller nums
        currentSmallerNum = x-1
        while (currentSmallerNum in numsSet):
            numsSet.remove(currentSmallerNum)
            currentSmallerNum -= 1
            count += 1

        if count > longestChain:
            longestChain = count
    return longestChain