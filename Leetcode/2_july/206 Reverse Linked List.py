# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None 
        h = head
        mylist = []
        while h:
            mylist.append(h.val)
            h = h.next
        # mylist.reverse()
        mh = ListNode()
        h = mh
        while mylist:
            
            h.val = mylist[len(mylist)-1]
            # print(mylist[len(mylist)-1],mh,h.val)
            mylist.pop()
            h.next = ListNode()
            h = h.next
            
        m = mh
        while m.next.next:
            m = m.next
            # print(m)
        else:
            m.next = None
        return mh