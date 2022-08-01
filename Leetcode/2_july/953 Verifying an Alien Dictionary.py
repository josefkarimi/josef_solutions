class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
		# create a mapping (char -> position) for O(1) lookups.
        char_to_idx = {c:i for i,c in enumerate(order)}
        
        prev = []        
        for i in range(len(words)):
			# Translate each character into its position in the alien alphabet.
            word = [char_to_idx[char] for char in words[i]]
            # print(word)
			
			# Check if the current word translated is not less then the previous one.
            if word < prev:
                return False
            prev = word
            
        return True


# Runtime: 72 ms, faster than 18.19% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.9 MB, less than 84.08% of Python3 online submissions for Verifying an Alien Dictionary.