# First and Last Occurrence

**Problem Links:**
https://bytebytego.com/exercises/coding-patterns/binary-search/find-the-insertion-index
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

**Initial thoughts:** Brute force way to solve this problem would be to iterate through each element and store the first index in which the target appears and the last index in which the target appears. This would be O(n) time complexity.

**Efficient Method:** We can instead use binary search to find one instance of the target. We now use the index of the instance to traverse its neighbouring values using binary search too in order to find the lowest and the highest index of the target.

| Leetcode Link | Time Complexity | Space Complexity | Solution beats % of LeetCoders |
| --- | --- | --- | --- |
| [First and Last Occurrence](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/) | O(log(n)) | O(1) | 100 |