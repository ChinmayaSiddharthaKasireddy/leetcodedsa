class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        word_set = set()
        result = []

        for word in words:
            if not word:
                continue

            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if word[j:i] in word_set:
                        dp[i] = True
                        break

            if dp[n]:
                result.append(word)

            word_set.add(word)

        return result
        