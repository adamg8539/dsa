def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    sList = list(s)
    for x in sList:
        if x == "(" or x == "{" or x == "[":
            stack.append(x)
            continue
        elif x == ")":
            if len(stack) == 0:
                return False
            xCheck = stack.pop()
            if xCheck == "(":
                continue
        elif x == "}":
            if len(stack) == 0:
                return False
            xCheck = stack.pop()
            if xCheck == "{":
                continue
        else:
            if len(stack) == 0:
                return False
            xCheck = stack.pop()
            if xCheck == "[":
                continue
        return False
    return len(stack) == 0