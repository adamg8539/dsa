def widthOfBinaryTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if root == None:
        return 0
    levelLeftDict = {}

    
    def addToDict(root, level, count):
        if not (level in levelLeftDict):
            levelLeftDict[level] = [count, count]
        else:
            levelLeftDict[level][1] = count            

        if root.left != None:
            addToDict(root.left, level + 1, 2*count)
        if root.right != None:
            addToDict(root.right, level + 1, 2*count+1)
    
    addToDict(root, 0, 1)
    
    finalWidth = 0
    for x in levelLeftDict.keys():
        if levelLeftDict[x][1] - levelLeftDict[x][0] + 1 > finalWidth:
            finalWidth = levelLeftDict[x][1] - levelLeftDict[x][0] + 1
    return finalWidth