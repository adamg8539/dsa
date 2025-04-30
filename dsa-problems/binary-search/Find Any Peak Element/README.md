# Find a Peak Element

**Problem Links:**
https://leetcode.com/problems/find-peak-element/description/

**Initial thoughts:** Brute force method would be to go through the array and check each value to see if the neighbouring values i-1 and i+1 are lower than the current. This would be O(n) time complexity since we would increment through the array one at a time.

**Efficient Method:** Since we just need to find 1 peak (not necessarily the highest peak), we can traverse the array via mid-points. At each mid-point, we check if its ascending or descending and we repeat the process until we find the peak. This way we don't have to go through every element and we achieve our goal in O(log(n)) complexity.

**Further Improvements to Efficiency:** Since we are told array[-1] = array[n] = -inf, we can do a quick check on the first and last element to see if they are peaks. This way, we have a chance of finding the peak with doing almost no work.

| Leetcode Link | Time Complexity | Space Complexity | Solution beats % of LeetCoders |
| --- | --- | --- | --- |
| [Two Sum II](https://leetcode.com/problems/find-peak-element/description/) | O(log(n)) | O(1) | 100 |