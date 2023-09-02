# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current_node = head
        val_list = []
        while current_node:
            val_list.append(current_node.val)
            current_node = current_node.next
        
        return val_list == val_list[::-1]
        # while next_node:
        #     val_list.append(next_node.val)
        #     next_node = next_node.next

        # if val_list[:len(val_list)//2] == val_list[(len(val_list)+1)//2:][::-1]:
        #     return True
        
        # return False