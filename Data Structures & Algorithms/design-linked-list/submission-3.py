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
        if not self.dummy.next:
            self.tail = ListNode(val=val)
            self.dummy.next = self.tail
        else:
            self.dummy.next = ListNode(val=val, next=self.dummy.next)
        
        self.n += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.n:
            return None

        if index == self.n:
            self.addAtTail(val)
            return None
        
        if index == 0:
            self.addAtHead(val)
            return None

        curr = self.dummy.next
        for i in range(index-1):
            curr = curr.next
        
        curr.next = ListNode(val, curr.next)
        self.n += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.n:
            return None
        
        curr = self.dummy.next
        
        if self.n == 0:
            self.tail = self.dummy
        
        if index == 0:
            self.dummy.next = self.dummy.next.next
            return None

        for i in range(index-1):
            curr = curr.next

        if index == self.n-1:
            curr.next = None
            self.tail = curr
        else:
            curr.next = curr.next.next
        
        self.n -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)