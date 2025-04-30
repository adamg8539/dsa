def middleNode(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    mid = head
    counter = 0
    while head != None:
        head = head.next
        if counter != 0:
            mid = mid.next
            counter = 0
            continue
        counter += 1
    return mid