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
            steps = 0 
            while el:
                # Maybe I can move this outside? Since individual LLs are sorted - no need to start checking from the start?
                while curr.next and el.val >= curr.next.val:
                    curr = curr.next
                    steps += 1
                if not steps: # Optimization 2: new list smaller than prev list(s)
                    dummy.next = el
                    break
                if curr.next:
                    node = ListNode(el.val, curr.next)
                    curr.next = node
                else: # optimization 1: new list > prev list(s)
                    node = ListNode(el.val)
                    curr.next = node
                    break

                
                el = el.next
            

        for i in range(1, len(lists)):
            if lists[i]:
                mergein(lists[i])
        
        return dummy.next