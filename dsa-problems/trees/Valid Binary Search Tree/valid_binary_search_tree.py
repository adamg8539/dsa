from binarytree import Node 
def isValidBST(self, root):
  """
  :type root: Optional[TreeNode]
  :rtype: bool
  """
  def verifyChildren(node, left, right):
    if node == None:
      return True

    if node.val >= right or node.val <= left:
      return False
    
    return (verifyChildren(node.left, left, node.val) and
      verifyChildren(node.right, node.val, right))
      
  return verifyChildren(root, float("-inf"), float("inf"))