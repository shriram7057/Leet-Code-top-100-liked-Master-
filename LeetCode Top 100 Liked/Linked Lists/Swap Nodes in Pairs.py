class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            cur.next, a.next, b.next = b, b.next, a
            cur = a
        return dummy.next
