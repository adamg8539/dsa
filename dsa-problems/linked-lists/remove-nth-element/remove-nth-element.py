def removeNthFromEnd(self, head, n):
  
  # Copy pasting this code in leetcode will work
  # For now I can't seem to find the import for the ListNode used in leetcode
  dummy = ListNode(0)
  dummy.next = head

  fast = slow = dummy

  # Move the fast pointer n steps ahead
  for _ in range(n):
      fast = fast.next

  # Move both pointers until fast reaches the end
  while fast.next:
      fast = fast.next
      slow = slow.next

  # Remove the nth node
  slow.next = slow.next.next

  return dummy.next
