def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[len(nums)-1] > nums[len(nums)-2]:
        return len(nums)-1
    low = 1
    high = len(nums)-1
    while low <= high:
        mp = (low+high)//2
        if nums[mp] > nums[mp + 1]:
            if nums[mp] > nums[mp - 1]:
                return mp
            else:
                high = mp - 1
        else:
            low = mp + 1
        
    return mp