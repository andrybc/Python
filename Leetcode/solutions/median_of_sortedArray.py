class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mid =(int)((len(nums1) + len(nums2))/2) 
        n = len(nums1) + len(nums2)
        median = 0
        num1Counter, num2Counter = 0,0
        mergedArray = []
        i = 0
        print(mid)
        while num1Counter < len(nums1) and num2Counter < len(nums2) and i <= mid:
                if nums1[num1Counter] <= nums2[num2Counter]:
                    print(nums1[num1Counter])
                    print(nums2[num2Counter])
                    mergedArray.append(nums1[num1Counter])
                    print(mergedArray)
                    num1Counter+=1
                    i+=1
                else:
                    mergedArray.append(nums2[num2Counter])
                    num2Counter+=1
                    i+=1
                    
        while num1Counter < len(nums1)  and i<= mid:
            mergedArray.append(nums1[num1Counter])
            num1Counter+=1
            i+=1

        while num2Counter < len(nums2) and i<= mid:
            mergedArray.append(nums2[num2Counter])
            num2Counter+=1
            i+=1
           
        print(mergedArray) 
  
        median = float((mergedArray[len(mergedArray)-1]) if n%2==1 else (mergedArray[len(mergedArray)-1] + mergedArray[len(mergedArray)-2])/2.0)   
        #print(median)
        return median