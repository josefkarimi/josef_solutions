class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1,len(arr)+1, 2):
            for ind in range(len(arr)-i+1):
                # print(f"ans:{ans} + arr:{arr[ind:ind+i]} // i = {i}, ind = {ind}")
                ans += sum(arr[ind:ind+i])
        return ans


# Runtime: 123 ms, faster than 32.62% of Python3 online submissions for Sum of All Odd Length Subarrays.
# Memory Usage: 13.8 MB, less than 64.21% of Python3 online submissions for Sum of All Odd Length Subarrays.