def reverseList(self, head):
    prev = None
    while head != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
    