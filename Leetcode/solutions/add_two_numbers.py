# solutions/add_two_numbers.py

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #print(l1)
        #print(l2)
        ansHead = ListNode()
        current = ansHead
        current_Carry = 0
        while l1 != None or l2 != None or current_Carry==1:
            #curr = current
            if l1==None and l2==None and current_Carry==1:
                current.val = current_Carry
                
            elif l1 == None:
                current.val = l2.val + current_Carry
                l2 = l2.next
            elif l2 == None:
                current.val = l1.val + current_Carry
                l1 = l1.next

            else:
                current.val = l1.val + l2.val + current_Carry
                l1 = l1.next
                l2 = l2.next
                
                
            if current.val >=10:
                current.val -=10
                current_Carry =1
            else:
                current_Carry = 0
            
            if l1 != None or l2!= None or current_Carry ==1:
                current.next = ListNode()
                current = current.next
              
        return ansHead  
         