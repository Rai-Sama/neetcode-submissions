class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.n = 0
        self.tail = self.dummy

    def get(self, index: int) -> int:
        if index >= self.n:
            return -1
        curr = self.dummy.next

        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.n += 1
        if not self.dummy.next:
            self.tail = ListNode(val=val)
            self.dummy.next = self.tail
        else:
            self.dummy.next = ListNode(val=val, next=self.dummy.next)

    def addAtTail(self, val: int) -> None:
        self.n += 1
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.n:
            return None

        if index == self.n:
            self.addAtTail(val)
            return None
        
        if index == 0:
            self.addAtHead(val)
            return None
        
        self.n += 1

        curr = self.dummy.next
        for i in range(index-1):
            curr = curr.next
        
        curr.next = ListNode(val, curr.next)
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.n:
            return None
        
        self.n -= 1
        curr = self.dummy.next
        for i in range(index-1):
            curr = curr.next

        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)