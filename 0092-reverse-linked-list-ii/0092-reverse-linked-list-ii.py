# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head

        idx = 1
        node = head
        left_node, pre_node, start_node = None, None, None

        while node and idx <= right:
            if idx > left:
                tmp = node
                node, tmp.next, pre_node = node.next, pre_node, tmp
            else:
                left_node, pre_node, start_node = pre_node, node, node
                node = node.next
            idx += 1

        start_node.next = node
        if left_node:
            left_node.next = pre_node
            return head
        else:
            return pre_node