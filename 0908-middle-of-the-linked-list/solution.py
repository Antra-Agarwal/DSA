# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        temp = head
        count = 0
        pos = 0

        while temp:
            count += 1
            temp = temp.next
        
        pos = count//2 + 1

        temp = head

        for i in range(1,pos):
            temp = temp.next
        
        head = temp
        return head


        

        
