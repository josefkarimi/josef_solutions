# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        slow, fast = head, head
        
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                return slow
        
            slow = slow.next
        
        return slow


# Runtime: 58 ms, faster than 21.90% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.9 MB, less than 55.26% of Python3 online submissions for Middle of the Linked List.