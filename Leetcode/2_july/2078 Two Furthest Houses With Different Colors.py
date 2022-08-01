class Solution:
    def maxDistance(self, colors: List[int]) -> int:
		#first pass
        l, r = 0, len(colors)-1
        dist = 0
        
        while r > l:
            if colors[r] != colors[l]:
                dist = r-l
				#slight performance increase, break out if you find it 
				#because it can't get bigger than this
                break 
            r -= 1
			
        #second pass, backwards
        l, r = 0, len(colors)-1
        while r > l:
            if colors[r] != colors[l]:
                dist = max(dist, r-l)
                break
            l += 1
        
        return dist



# Runtime: 68 ms, faster than 46.10% of Python3 online submissions for Two Furthest Houses With Different Colors.
# Memory Usage: 13.8 MB, less than 59.53% of Python3 online submissions for Two Furthest Houses With Different Colors.