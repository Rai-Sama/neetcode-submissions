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

        def dvc(l, r):
            if l == r:
                return lists[l]
            
            mid = (l + r)//2
            l1 = dvc(l, mid)
            l2 = dvc(mid + 1, r)

            return mergein(l1, l2)
        
        return dvc(0, len(lists) - 1)