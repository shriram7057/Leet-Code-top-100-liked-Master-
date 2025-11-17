class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        dummy = ListNode()
        cur = dummy
        
        while h:
            val, i, node = heapq.heappop(h)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        
        return dummy.next
