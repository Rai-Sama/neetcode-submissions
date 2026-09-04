class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.head = self.dummy
        self.tail = self.dummy
        self.n = 0

    def get(self, index: int) -> int:
        
        if index >= self.n:
            return -1
        
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        
        node = ListNode(val)

        if self.n == 0: # First element
            self.head = node
            self.dummy.next = self.head
            self.tail = self.head
        else: # Existing
            self.dummy.next = node
            node.next = self.head
            self.head = node
        self.n += 1

    def addAtTail(self, val: int) -> None:
        
        node = ListNode(val)

        # this is the first element
        if self.n == 0:
            self.head = node
            self.dummy.next = self.head
            self.tail = self.head
        
        # there are existing elements
        else:
            self.tail.next = node
            self.tail = node
        
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        node = ListNode(val)
        
        # index invalid
        if index > self.n:
            return None

        # index valid
        ## index = 0 -> head
        if index == 0:
            self.addAtHead(val)
        ## index = n -> tail
        elif index == self.n:
            self.addAtTail(val)
        
        ## index in [1, n-1]
        else:
            curr = self.head
            prev = self.dummy
            while index:
                prev = curr
                curr = curr.next
                index -= 1
            prev.next = node
            node.next = curr
            self.n += 1
            

    def deleteAtIndex(self, index: int) -> None:
        # index invalid
        if index >= self.n:
            return None
        
        if index == 0 and self.n == 1:
            self.dummy.next = None
            self.head = self.tail = self.dummy
            self.n -= 1
            return None

        curr = self.head
        prev = self.dummy
        indx = index
        while indx:
            prev = curr
            curr = curr.next
            indx -= 1
            
        prev.next = curr.next
        if index == self.n-1:
            self.tail = prev
        
        if index == 0:
            self.head = curr.next
        
        self.n -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)