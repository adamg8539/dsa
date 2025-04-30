def hasCycle(self, head):
    fastP = head
    counter = 0
    while fastP != None:
        fastP = fastP.next
        if counter != 0:
            head = head.next
            if head == fastP:
                return True
            counter = 0
            continue
        counter +=1
    return False