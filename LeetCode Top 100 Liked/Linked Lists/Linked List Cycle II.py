class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow
