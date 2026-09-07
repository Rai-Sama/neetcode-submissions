# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergein(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        head = lists[0]
        
        for i in range(1, len(lists)):
            if lists[i]:
                head = mergein(head, lists[i])
        
        return head