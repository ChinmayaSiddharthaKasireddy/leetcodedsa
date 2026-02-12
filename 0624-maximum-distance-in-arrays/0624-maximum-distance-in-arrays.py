class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize with first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        max_distance = 0
        
        # Iterate from second array
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Compare with global min and max
            max_distance = max(max_distance, 
                               abs(current_max - min_val),
                               abs(max_val - current_min))
            
            # Update global min and max
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_distance

        