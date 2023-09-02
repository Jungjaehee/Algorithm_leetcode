# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return
        elif not l1:
            return l2
        elif not l2:
            return l1

        num = (l1.val + l2.val) // 10
        result = ListNode((l1.val + l2.val)%10)
        node1 = l1.next
        node2 = l2.next
        res_node = result

        while node1 or node2:
            if not node1:
                sums = node2.val + num
                node2 = node2.next
            elif not node2:
                sums = node1.val + num
                node1 = node1.next
            else:
                sums = node1.val+node2.val + num
                node1 = node1.next
                node2 = node2.next

            num = sums // 10
            res_node.next = ListNode(sums % 10)
            res_node = res_node.next


        if num:
            res_node.next = ListNode(num)

        return result