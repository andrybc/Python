class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Binary search logic
            if i < m and nums1[i] < nums2[j - 1]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                # Median calculation
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return max_of_left  # Odd length, single middle element
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0

        
            
        
        # mid =(int)((len(nums1) + len(nums2))/2) 
        # n = len(nums1) + len(nums2)
        # median = 0
        # num1Counter, num2Counter = 0,0
        # mergedArray = []
        # i = 0
        # print(mid)
        # while num1Counter < len(nums1) and num2Counter < len(nums2) and i <= mid:
        #         if nums1[num1Counter] <= nums2[num2Counter]:
        #             print(nums1[num1Counter])
        #             print(nums2[num2Counter])
        #             mergedArray.append(nums1[num1Counter])
        #             print(mergedArray)
        #             num1Counter+=1
        #             i+=1
        #         else:
        #             mergedArray.append(nums2[num2Counter])
        #             num2Counter+=1
        #             i+=1
                    
        # while num1Counter < len(nums1)  and i<= mid:
        #     mergedArray.append(nums1[num1Counter])
        #     num1Counter+=1
        #     i+=1

        # while num2Counter < len(nums2) and i<= mid:
        #     mergedArray.append(nums2[num2Counter])
        #     num2Counter+=1
        #     i+=1
           
        # print(mergedArray) 
  
        # median = float((mergedArray[len(mergedArray)-1]) if n%2==1 else (mergedArray[len(mergedArray)-1] + mergedArray[len(mergedArray)-2])/2.0)   
        # #print(median)
        # return median