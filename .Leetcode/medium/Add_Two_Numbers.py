class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        prev = None
        carry = 0
        
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            l1.val = val % 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
            
        if l2:
            prev.next = l2
            l1 = l2
            
        while carry and l1:
            val = l1.val + carry
            carry = val // 10
            l1.val = val % 10
            prev = l1
            l1 = l1.next
            

        if carry:
            prev.next = ListNode(carry)
            
        return head
