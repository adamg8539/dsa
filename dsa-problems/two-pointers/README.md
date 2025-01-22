# Pair Sum Sorted

**Problem**: Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Problem Links:
https://bytebytego.com/exercises/coding-patterns/two-pointers/pair-sum-sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Initial thoughts: Pointer 1 set to the first element. Pointer 2 iterating through the array to check if the sum of the values at each of the pointers matches the target sum. This solution is O(n^2). The problem here is that we aren't using the fact that the array is sorted to our advantage.

Efficient Method: Since the array is sorted, we can set one pointer to the start of the array and another to the end. Pointer 1 will represent the lowest value in the array and Pointer 2 will represent the highest value. If the sum of these two values is greater than our target, we decrement pointer 2 to point to a smaller value. If the sum is smaller than target, we increment pointer 1 to point to a greater value. We keep doing this till either pointer 1 passes pointer 2 or we find our target sum.

Subtlties which I think help the algorithm but which are hard to prove and quantify: When doing the if statements within the loop, the order is important. If we compare if our sums as equal to the target first, every iteration will compare this. The chances of the sum being equal to target are: 1/n! where as chances of being greater than or smaller than the target are close to 50% thus it is important to do the greater than or smaller than checks first.