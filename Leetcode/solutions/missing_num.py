class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(range(len(nums)+1))
        #print(num_set)
        
        for i in nums:
            num_set.remove(i)
            
        return num_set.pop()
    
        #mathematical approach
        # n = len(nums)
        # total_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return total_sum - actual_sum       