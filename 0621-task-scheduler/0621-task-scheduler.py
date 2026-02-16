class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = list(freq.values()).count(maxFreq)
        
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)

        