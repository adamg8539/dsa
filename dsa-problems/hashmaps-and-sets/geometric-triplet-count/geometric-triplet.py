from typing import List

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    # Write your code here
    pass
    numsMap = {}
    for x,y in enumerate(nums):
        if (y in numsMap):
            numsMap[y].append(x)
            continue
        numsMap[y] = [x]
    output = 0
    for w, x in enumerate(nums):
        if (r*x in numsMap):
            for a in numsMap[r*x]:
                if a > w:
                    if (r*r*x in numsMap):
                        for b in numsMap[r*r*x]:
                            if b > a:
                                output += 1
    return output