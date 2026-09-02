# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        curr = ListNode()
        head = None
        while i is not None and j is not None:
            if i.val <= j.val:
                if head is None:
                    head = i
                    curr = i
                else:
                    curr.next = i
                    curr = i
                i = i.next
            
            else:
                if head is None:
                    head = j
                    curr = j
                else:
                    curr.next = j
                    curr = j
                j = j.next
        
        while i is not None:
            if head is None:
                head = i
            else:
                curr.next = i
            curr = i
            i = i.next

        while j is not None:
            if head is None:
                head = j
            else:
                curr.next = j
            curr = j
            j = j.next
        
        return head