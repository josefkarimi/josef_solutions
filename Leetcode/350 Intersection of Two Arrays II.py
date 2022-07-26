class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        for num in nums1:
            if num not in dic1:
                dic1[num] = 1
            else:
                dic1[num] += 1
                
        dic2 = {}
        for num in nums2:
            if num not in dic2:
                dic2[num] = 1
            else:
                dic2[num] += 1
        ans = []
        for num in dic1:
            if num in dic2:
                for _ in range(min(dic1[num],dic2[num])):
                    ans.append(num)
            
        print(dic1, dic2)
        return ans



# Runtime: 94 ms, faster than 27.64% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.2 MB, less than 15.54% of Python3 online submissions for Intersection of Two Arrays II.