from ds import TreeNode

def balanced_binary_tree_validation(root: TreeNode) -> bool:
    # Write your code here
    pass
    if not root:
        return True

    def is_balanced(root: TreeNode):

        left, right = is_balanced(root.left), is_balanced(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max (left[1], right[1])]

    return is_balanced(root)[0]