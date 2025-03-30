from ds import TreeNode

def invert_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    rl = root.left
    root.left = root.right
    root.right = rl

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root