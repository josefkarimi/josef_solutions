class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))
        n = n[:1:-1]
        while len(n) != 32:
            n += "0"
        n = "0b" + n
        return (int(n, 2))


# Runtime: 39 ms, faster than 81.08% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.8 MB, less than 49.31% of Python3 online submissions for Reverse Bits.