# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2) :
#         len_l1, len_l2, jam = len(l1), len(l2), 0
#         for i in range(len_l1):
#             jam += l1[i] * (10 ** (len_l1 - i - 1))
#             print(jam) 
#         for i in range(len_l2):
#             jam += l2[i] * (10 ** (len_l2 - i - 1))
#             print(jam)
#         if len_l1 >= len_l2:
#             lis = []
#             for i in range(len_l1):
#                 r = int(((jam % (10 ** (i+1))) - (jam % (10 ** (i)))) / (10 ** (i)))
#                 lis.append(r)
#         if len_l2 > len_l1:
#             lis = []
#             for i in range(len_l2):
#                 r = int(((jam % (10 ** (i+1))) - (jam % (10 ** (i)))) / (10 ** (i)))
#                 lis.append(r)
#         return lis
# A = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])
# print(A,)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        for i in
        