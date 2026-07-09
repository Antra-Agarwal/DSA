# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        k %= n

        if k == 0:
            return head

        new_head = nodes[n - k]
        new_tail = nodes[n - k - 1]
        old_tail = nodes[-1]

        old_tail.next = head
        new_tail.next = None

        return new_head
