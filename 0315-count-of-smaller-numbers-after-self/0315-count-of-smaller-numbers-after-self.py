class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        # Store (value, original_index)
        enum = list(enumerate(nums))
        
        def merge_sort(arr):
            mid = len(arr) // 2
            if mid:
                left = merge_sort(arr[:mid])
                right = merge_sort(arr[mid:])
                
                m = len(left)
                n = len(right)
                i = j = 0
                merged = []
                
                while i < m or j < n:
                    if j == n or (i < m and left[i][1] <= right[j][1]):
                        # Count how many right elements have been used
                        result[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                        
                return merged
            return arr
        
        merge_sort(enum)
        return result
        