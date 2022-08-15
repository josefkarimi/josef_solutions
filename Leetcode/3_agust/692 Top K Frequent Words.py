from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        words = Counter(words).most_common()
        ans = []
        for i in range(k):
            ans.append(words[i][0])
        return ans 



# Runtime: 105 ms, faster than 27.76% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14 MB, less than 64.69% of Python3 online submissions for Top K Frequent Words.