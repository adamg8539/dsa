def getIntersectionNode(self, headA, headB):

    curA, curB = headA, headB
    a,b = 0,0
    while curA:
        a+=1
        curA = curA.next
    while curB:
        b+=1
        curB = curB.next

    if a > b:
        while a != b:
            headA = headA.next
            a -= 1
    if b > a:
        while b != a:
            headB = headB.next
            b -= 1
    
    while headA != None:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None
