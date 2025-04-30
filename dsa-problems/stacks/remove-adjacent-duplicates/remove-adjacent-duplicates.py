def removeDuplicates(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for x in s:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    return ''.join(stack)