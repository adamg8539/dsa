from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # set pointer 1 to start of the array (smallest possible value)
    p1 = 0
    # set pointer 2 to end of the array (largest possible value)
    p2 = len(nums)-1
    while (p1 < p2):
        sum = nums[p1] + nums[p2]
        if sum < target:
            p1 += 1
        elif sum > target:
            p2 -= 1
        # if sum is not greater than and it is not smaller than target, it must be equal to target
        else:
            return [p1+1, p2+1]
    return []
