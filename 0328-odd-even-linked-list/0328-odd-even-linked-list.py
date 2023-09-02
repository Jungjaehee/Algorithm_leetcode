# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sub = head.next
        node = head

        while node and node.next:
            odd, even = node, node.next
            node = node.next.next

            if odd.next.next:
                odd.next = odd.next.next
            else:
                odd.next = sub
            if even.next and even.next.next:
                even.next = even.next.next
            else:
                even.next = None

        if node:
            node.next = sub

        return head
