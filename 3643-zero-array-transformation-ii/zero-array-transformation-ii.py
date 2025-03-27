class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
  
        def validator(mid):
            # This function checks if using the first `mid` queries (actually mid queries, not mid index) 
            # can make the array all zero or more (total[i] >= nums[i])
            
            array = (len(nums) + 1) * [0] 
            prefix_sum = 0
            total = []

            # We should apply `mid` number of queries (not index), so we loop from 0 to mid - 1
            for i in range(mid):
                left = queries[i][0]
                right = queries[i][1]
                val = queries[i][2]
                array[left] += val
                array[right + 1] -= val
           
            for i in range(len(nums)):  # Only need prefix sum up to len(nums), not full array
                prefix_sum += array[i]
                total.append(prefix_sum)

            # Return whether total applied at each index is at least the required value
            return all(t >= n for t, n in zip(total, nums))

        # Binary search setup: we want to check from 0 to len(queries)
        low = 0
        high = len(queries)

        # First check if the entire set of queries still can't make the array zero — early return -1
        if not validator(high):
            return -1

        # Binary search for the smallest k where array becomes zero
        while low <= high:
            mid = (low + high) // 2
            if validator(mid):  # Can transform with mid queries
                high = mid - 1
            else:               # Need more queries
                low = mid + 1

        # At the end of binary search, low will be the smallest number of queries needed
        return low
