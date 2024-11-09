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
        #previous accepted code
        #print(l1)
        #print(l2)
        # ansHead = ListNode()
        # current = ansHead
        # current_Carry = 0
        # while l1 != None or l2 != None or current_Carry==1:
        #     curr = current
        #     if l1==None and l2==None and current_Carry==1:
        #         curr.val = current_Carry
                
        #     elif l1 == None:
        #         curr.val = l2.val + current_Carry
        #         l2 = l2.next
        #     elif l2 == None:
        #         curr.val = l1.val + current_Carry
        #         l1 = l1.next

        #     else:
        #         curr.val = l1.val + l2.val + current_Carry
        #         l1 = l1.next
        #         l2 = l2.next
                
                
        #     if curr.val >=10:
        #         curr.val -=10
        #         current_Carry =1
        #     else:
        #         current_Carry = 0
            
        #     if l1 != None or l2!= None or current_Carry ==1:
        #         current.next = ListNode()
        #         current = current.
                
        #cleaned up code      
        sumHead = ListNode()
        current_node = sumHead
        carry = 0
        while  l1  or  l2  or carry:
            current_node.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = current_node.val //10
            current_node.val %= 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            if l1 or l2 or carry:
                current_node.next = ListNode()
                current_node = current_node.next
              
        return sumHead  
              
    
         