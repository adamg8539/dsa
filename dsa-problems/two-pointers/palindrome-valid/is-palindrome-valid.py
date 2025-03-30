def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    c1, c2 = 0, len(s)-1

    while (c1 < c2):
        if not (s[c1].isalnum()):
            c1 += 1
            continue
        if not (s[c2].isalnum()):
            c2 -= 1
            continue
        if (s[c1] != s[c2]):
            if s[c1].lower() != s[c2].lower():
                return False
        c1 += 1
        c2 -= 1
    return True