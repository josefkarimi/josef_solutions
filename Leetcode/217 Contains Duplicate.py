class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums :
            if nums.count(num) > 1 :
                return True 
        return False 

# 65 / 70 test cases passed.
# 	Status: Time Limit Exceeded


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set(nums)
        # print(numbers)
        return len(nums) != len(numbers)


# Runtime: 874 ms, faster than 14.14% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 30.56% of Python3 online submissions for Contains Duplicate.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))



# Runtime: 794 ms, faster than 25.96% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26 MB, less than 72.31% of Python3 online submissions for Contains Duplicate.