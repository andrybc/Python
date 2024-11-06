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
        ansHead = ListNode()
        current = ansHead
        current_Carry = 0
        while l1 != None or l2 != None:
            curr = current
            if l1 == None:
                curr.val = l2.val + current_Carry
            if l2 == None:
                curr.val = l1.val + current_Carry
            curr.val = l1.val + l2.val + current_Carry
            l1 = l1.next
            l2 = l2.next
            if curr.val >=10:
                curr.val -=10
                current_Carry =1
            else:
                current_Carry = 0
            
            if l1 != None or l2!= None or current_Carry ==1:
                current.next = ListNode()
                current = current.next
              
        return ansHead  
        