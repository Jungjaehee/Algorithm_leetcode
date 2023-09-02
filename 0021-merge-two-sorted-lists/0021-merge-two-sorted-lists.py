# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            new_list = ListNode(val=list1.val)
            first_node = list1.next
            sec_node = list2

        else:
            new_list = ListNode(val=list2.val)
            first_node = list1
            sec_node = list2.next

        tmp_node = new_list
        while first_node is not None or sec_node is not None:
            if first_node is None:
                tmp_node.next = sec_node
                break
            elif sec_node is None:
                tmp_node.next = first_node
                break

            if first_node.val > sec_node.val:
                tmp_node.next = ListNode(val=sec_node.val)
                tmp_node = tmp_node.next
                sec_node = sec_node.next
            else:
                tmp_node.next = ListNode(val=first_node.val)
                tmp_node = tmp_node.next
                first_node = first_node.next

        return new_list
