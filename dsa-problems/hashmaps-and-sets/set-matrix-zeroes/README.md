# Set Matrix Zeroes

**Problem Links:**
https://leetcode.com/problems/set-matrix-zeroes/

**Initial thoughts:** Brute force solution would be to go through each value in the 2d matrix and use another matrix to store all the values that need to be zeroed out. Once the entire process is done, the zeroes can be trasposed onto the original matrix. This would be very inefficient in terms of space complexity as it would require O(n) space and would require O(n^2) time complexity.

**Efficient Method:** For an efficient solution, we can use the first row and first column of the current matrix as placeholder for which rows and columns need to be converted to 0s. We must be careful as the 0,0 value would overlap in the first row and first column. Thus we would make use of a variable to store one of these values. Once the whole matrix is searched for zeroes and the corresponding values in the first column/row would be set to zero. These values can then be used to set all the other required values to 0. Time complexity would be O(n) since we are iterating through the whole matrix. Space complexity would be O(1) since most computations are done in place.

| Leetcode Link | Time Complexity | Space Complexity | Solution beats % of LeetCoders |
| --- | --- | --- | --- |
| [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | O(n) | O(n) | 78 |