# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        mystr = ""
        while head:
            mystr += str(head.val)
            head = head.next
        return int(mystr,2)



# Runtime: 57 ms, faster than 25.25% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 13.8 MB, less than 95.27% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.