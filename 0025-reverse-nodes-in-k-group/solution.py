class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev = end
            curr = start

            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        while True:
            node = before

            for _ in range(k):
                node = node.next
                if node is None:
                    return dummy.next

            group_start = before.next
            group_end = node.next

            before.next = reverse(group_start, group_end)
            before = group_start
