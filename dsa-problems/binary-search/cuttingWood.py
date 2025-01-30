from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    # Write your code here
    pass
    high = 0
    for x in heights:
        if x > high:
            high = x
    
    if k == 0:
        return high
    low = 0
    while low <= high:
        woodCount = 0
        mid = midpoint(low, high)
        for x in heights:
            if x > mid:
                woodCount += (x - mid)
        if woodCount < k:
            high = mid - 1
        elif woodCount > k:
            low = mid + 1
        else:
            return mid
        
    return high

def midpoint(low: int, high: int) -> int:
    return (low+high)//2