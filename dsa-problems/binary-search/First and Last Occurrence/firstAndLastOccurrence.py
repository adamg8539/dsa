from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
    # Write your code here
    pass
    if len(nums) == 0:
        return [-1, -1]
    low = 0
    high = len(nums)-1
    retHigh = -1
    retLow = -1
    if nums[0] == target:
        retLow = 0
    if nums[high] == target:
        retHigh = high
    midIndex = 0
    while low <= high:
        midIndex = midpoint(low, high)
        if nums[midIndex] > target:
            high = midIndex - 1
        elif nums[midIndex] < target:
            low = midIndex + 1
        else:
            break

    if nums[midIndex] != target:
        return [-1, -1]
    
    if retLow == -1:
        retLow = low
        newHigh = midIndex
        while retLow <= newHigh:
            mp = midpoint(retLow, newHigh)
            if nums[mp] == target:
                if nums[mp-1] != target:
                    retLow = mp
                    break
                newHigh = mp - 1
            else:
                retLow = mp + 1

    if retHigh == -1:
        retHigh = high
        newLow = midIndex
        while retHigh >= newLow:
            mp = midpoint(newLow, retHigh)
            if nums[mp] == target:
                if nums[mp+1] != target:
                    retHigh = mp
                    break
                newLow = mp + 1
            else:
                retHigh = mp - 1

    return [retLow, retHigh]


def midpoint(low: int, high: int) -> int:
    return (low + high)//2











#     def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
#     # Write your code here
#     pass
#     if len(nums) == 0:
#         return [-1, -1]
#     low = 0
#     high = len(nums)-1
#     midIndex = 0
#     while low <= high:
#         midIndex = midpoint(low, high)
#         if nums[midIndex] > target:
#             high = midIndex - 1
#         elif nums[midIndex] < target:
#             low = midIndex + 1
#         else:
#             low = midIndex
#             high = midIndex
#             break
    
#     if nums[midIndex] != target:
#         return [-1, -1]
#     while low >= 0:
#         if nums[low] == target:
#             low -= 1
#         else:
#             low += 1
#             break
#     while high <= len(nums)-1:
#         if nums[high] == target:
#             high += 1
#         else:
#             high -= 1
#             break
#     if low < 0:
#         low = 0
#     if high > len(nums)-1:
#         high = len(nums)-1
#     return [low, high]


# def midpoint(low: int, high: int) -> int:
#     return (low + high)//2
    