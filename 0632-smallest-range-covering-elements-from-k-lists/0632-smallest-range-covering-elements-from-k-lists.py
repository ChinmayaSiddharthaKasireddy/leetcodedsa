import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        k = len(nums)
        heap = []
        current_max = float('-inf')
        
        # Step 1: Put first element of each list in heap
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, val)
        
        best_range = [float('-inf'), float('inf')]
        
        # Step 2: Process heap
        while True:
            current_min, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update best range
            if (current_max - current_min < best_range[1] - best_range[0] or
                (current_max - current_min == best_range[1] - best_range[0] and
                 current_min < best_range[0])):
                best_range = [current_min, current_max]
            
            # Move to next element in same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # One list exhausted → cannot cover all lists anymore
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            
            # Update current max
            current_max = max(current_max, next_val)
        
        return best_range
        