def isSymmetric(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if not root:
        return True

    if root.left == None and root.right == None:
        return True
    
    def mirrorRoot(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        if not mirrorRoot(root1.left, root2.right):
            return False
        if not mirrorRoot(root1.right, root2.left):
            return False
        return True

    return mirrorRoot(root.left, root.right)