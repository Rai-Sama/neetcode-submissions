# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        head = lists[0]
        dummy = ListNode()
        dummy.next = head
        
        def mergein(lst):
            
            el = lst
            curr = dummy 
            while el:
                # Maybe I can move this outside? Since individual LLs are sorted - no need to start checking from the start?
                while curr.next and el.val >= curr.next.val:
                    curr = curr.next
                
                if curr.next:
                    node = ListNode(el.val, curr.next)
                else:
                    node = ListNode(el.val)
                curr.next = node
                
                el = el.next
            

        for i in range(1, len(lists)):
            if lists[i]:
                mergein(lists[i])
        
        return dummy.next