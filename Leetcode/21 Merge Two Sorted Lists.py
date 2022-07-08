# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mylist = ListNode()
        a = list1
        b = list2
        m = mylist
        if a == b == None:
            return None

        while a and b:
            if a.val <= b.val:
                m.val = a.val
                a = a.next
                m.next = ListNode()
                m = m.next
                print("1")
            else:
                m.val = b.val
                b = b.next
                m.next = ListNode()
                m = m.next
                print("2")
        else : 
            while a :
                m.val = a.val
                a = a.next
                m.next = ListNode()
                m = m.next
                print("a")
            while b:
                m.val = b.val
                b = b.next
                m.next = ListNode()
                m = m.next
                print("b")  

        m = mylist
        while m.next.next:
            m = m.next
            print(m)
        else:
            m.next = None
        print(mylist)   
        return(mylist)