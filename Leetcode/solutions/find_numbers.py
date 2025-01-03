class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1]*= -1
        
        print(nums)
        
        for i in range(len(nums)):
            if nums[i]> 0:
              ans.append(i+1)
              
        return ans