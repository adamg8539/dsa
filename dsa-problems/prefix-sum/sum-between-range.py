from typing import List

class SumBetweenRange:
    def __init__(self, nums: List[int]):
        pass
        prefixSum = 0
        prefixArr = []
        for x in nums:
            prefixSum += x
            prefixArr.append(prefixSum)
        self.prefixArr = prefixArr

    def sum_range(self, i: int, j: int):
        pass
        if i == 0:
            return self.prefixArr[j]
        return self.prefixArr[j]-self.prefixArr[i-1]