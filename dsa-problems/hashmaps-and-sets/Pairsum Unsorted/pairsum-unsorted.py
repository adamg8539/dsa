from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    pass
    obj = []
    d1 = {y:x for x,y in enumerate(nums)}
    for a,b in enumerate(nums):
        if (a in obj):
            continue
        newT = target - b
        if (newT in d1.keys() and d1.get(newT) != a):
            obj.append(a)
            obj.append(d1.get(newT))
            continue
    return obj