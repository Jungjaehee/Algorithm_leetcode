# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head:
        #     rev.next = ListNode(self.reverseList(head.next))
        #     return rev
        
        if not head: return
        rev = None
        node = head

        while node:
            rev = ListNode(node.val, rev)
            node = node.next

        return rev