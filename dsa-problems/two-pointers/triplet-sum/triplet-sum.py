def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()

    output = []
    x = 0

    while x < len(nums)-2:
        target = 0 - nums[x]
        y = len(nums)-1
        z = x+1
        while z < y:
            if nums[z] + nums[y] > target:
                y = y-1
            elif nums[z] + nums[y] < target:
                z = z+1
            else:
                output.append([nums[x], nums[y], nums[z]])
                while nums[z] == nums[z+1] and z < y-1:
                    z += 1
                while nums[y] == nums[y-1] and y > z+1:
                    y -= 1
                z += 1
                y -= 1
        while nums[x] == nums[x+1] and x < len(nums)-3:
            x += 1
        x += 1        
    return output  