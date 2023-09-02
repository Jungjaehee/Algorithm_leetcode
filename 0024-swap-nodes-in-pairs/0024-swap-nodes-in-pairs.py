# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        tmp_node = head

        if head.next:
            head = head.next

        while tmp_node and tmp_node.next:
            first_node, second_node = tmp_node, tmp_node.next
            tmp_node = tmp_node.next.next

            if second_node.next and second_node.next.next:
                first_node.next = second_node.next.next
            else:
                first_node.next = second_node.next

            second_node.next = first_node

        return head