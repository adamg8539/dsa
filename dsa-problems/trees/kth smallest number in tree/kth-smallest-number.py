def kthSmallest(self, root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """
    finalArr = []
    curr = root
    while curr != None:
        if len(finalArr) == k:
            break
        if curr.left == None:
            finalArr.append(curr.val)
            curr = curr.right
        else:
            pred = curr.left
            while pred.right != None and pred.right != curr:
                pred = pred.right
            if pred.right == None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                finalArr.append(curr.val)
                curr = curr.right

    return finalArr[k-1]