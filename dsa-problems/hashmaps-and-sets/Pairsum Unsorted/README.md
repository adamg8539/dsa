# Find Pair Sum

**Problem Links:**
https://leetcode.com/problems/two-sum/description/

**Initial thoughts:** Brute force method to solve this would be to inspect every single pair of values available. To imagine this we can create a 2d matrix out of all possible values and check each point to see if the value is equal to the target.

**Efficient Method:** We store all the values and its corresponding indexes to a hash map. We iterate over the array and for each value, we try find (target-current_value) in the hash map. If it exists, we have found the correct pair sum and we return the indices of the two numbers.

| Leetcode Link | Time Complexity | Space Complexity | Solution beats % of LeetCoders |
| --- | --- | --- | --- |
| [Pair Sum](https://leetcode.com/problems/two-sum/description/) | O(n) | O(n) | 100 |