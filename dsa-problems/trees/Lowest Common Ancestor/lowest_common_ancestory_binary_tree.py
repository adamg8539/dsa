from ds import TreeNode
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Write your code here
    pass
    def in_subtree(node: TreeNode, p: TreeNode):
        if node == p:
            return True
        
        if node.left != None:
            if in_subtree(node.left, p):
                return True
        
        if node.right != None:
            if in_subtree(node.right, p):
                return True

        return False
        


    finalRoot = root
        
    if root.left and in_subtree(root.left, p) and in_subtree(root.left, q):
        finalRoot = lowest_common_ancestor(root.left, p, q)
    elif root.right and in_subtree(root.right, p) and in_subtree(root.right, q):
        finalRoot = lowest_common_ancestor(root.right, p, q)
    return finalRoot