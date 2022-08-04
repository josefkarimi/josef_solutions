# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            node_dict = {}

            while head:
                # if node is not in dict, add it.
                if head not in node_dict:
                    node_dict[head] = 'visited'
                # our node is in dict, so we have seen this node and this node is the start point of our cycle.
                else:
                    return head
                # go to next node
                head = head.next
            # return None if there is no cycle.
            return None




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        while head:
            if head not in nodes:
                nodes.add(head)
                head = head.next
            else:
                return head
        return -1
                



# Runtime: 56 ms, faster than 89.29% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 18 MB, less than 10.30% of Python3 online submissions for Linked List Cycle II.