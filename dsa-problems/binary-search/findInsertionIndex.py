from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    # Write your code here
    pass
    if len(nums) == 0:
        return 0
    low = 0
    high = len(nums) - 1
    while (low <= high):
        midIndex = midPoint(low, high)
        if nums[midIndex] > target:
            high = midIndex - 1
        elif nums[midIndex] < target:
            low = midIndex + 1
        else:
            return midIndex
    if target > nums[midIndex]:
        return midIndex+1
    return midIndex


def midPoint(low: int, high: int) -> int:
    return (low + high) // 2