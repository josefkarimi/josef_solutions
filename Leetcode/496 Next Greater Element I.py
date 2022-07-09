class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in range(len(nums1)):
            for i in range(nums2.index(nums1[n]),len(nums2)):
                if nums1[n] < nums2[i]:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)
        return(ans)