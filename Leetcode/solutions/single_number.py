class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # seen_once = set()
        
        # for i in nums:
        #     if i in seen_once:
        #         seen_once.remove(i)
        #     else:
        #         seen_once.add(i)
            
        
        # return seen_once.pop()
    #using the XOR property

        ans = 0
        for i in nums:
           ans ^= i
           
        return ans