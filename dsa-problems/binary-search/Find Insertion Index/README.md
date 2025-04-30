# Find Insertion Index

**Problem Links:**
https://bytebytego.com/exercises/coding-patterns/binary-search/find-the-insertion-index
https://leetcode.com/problems/search-insert-position/description/

**Initial thoughts:** Brute force way to solve this problem would be to iterate through each element and find the first element which is greater than the target and return its index value. The time complexity here would be O(n).

**Efficient Method:** Since we know that the given array is sorted, we can use binary search to split the array in half each time until we either find the target in the array or find the first element greater than the target. This allows us to achieve time complexity of O(log(n))

| Leetcode Link | Time Complexity | Space Complexity | Solution beats % of LeetCoders |
| --- | --- | --- | --- |
| [Two Sum II](https://leetcode.com/problems/find-peak-element/description/) | O(log(n)) | O(1) | 100 |