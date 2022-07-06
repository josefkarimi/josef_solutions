class Solution:
    def twoSum(self, nums, target):
        d = target / 2
        if d in nums:
            num2 = [i for i in nums]
            ind = [nums.index(d)]
            num2.remove(d)
            if d in num2 :
                ind.append(nums2.index(d)+1)
                return ind
            else:
                for i in nums:
                    x = target - i
                    # print(nums, num2)
                    if x in nums:
                        if nums.index(x) == nums.index(i):
                            pass
                        else:
                            return [nums.index(i), nums.index(x)]
        else:
            for i in nums:
                x = target - i
                if x in nums:
                    return [nums.index(i),nums.index(x)]
x = Solution().twoSum([3, 2, 4] ,6)
print (x)