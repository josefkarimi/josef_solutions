class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        try:
            i = nums.index(target)
            for n in range(i, len(nums)):
                if nums[n] == target :
                    ans.append(n)
                else:
                    break
            return ans
        except:
            return []




# Runtime: 52 ms, faster than 88.66% of Python3 online submissions for Find Target Indices After Sorting Array.
# Memory Usage: 14 MB, less than 18.29% of Python3 online submissions for Find Target Indices After Sorting Array.