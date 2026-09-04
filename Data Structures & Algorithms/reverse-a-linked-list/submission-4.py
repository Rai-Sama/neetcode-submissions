# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def recursiverev(head):
    node = head.next
    if node.next:
        tail = recursiverev(node)
        node.next = head
        return tail
    else:
        node.next = head
        return node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # RECURSION PRACTICE
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        tail = recursiverev(dummy)
        head.next = None
        return tail