def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    largestArea = 0
    c1, c2 = 0, len(height)-1
    while(c1 < c2):
        if (height[c1] > height[c2]):
            checkArea = height[c2] * (c2 - c1)
            c2 -= 1
        else:
            checkArea = height[c1] * (c2 - c1)
            c1 += 1
        if checkArea > largestArea:
            largestArea = checkArea
    return largestArea