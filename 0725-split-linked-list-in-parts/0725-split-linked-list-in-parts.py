class Solution:
    def getSize(self, head: Optional[ListNode]) -> int:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        return n

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.getSize(head)
        result = []
        div = int(n / k)
        rest = n % k
        current = head

        for i in range(k):
            part_head = current
            part_size = div + 1 if i < rest else div

            for j in range(part_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            result.append(part_head)

        return result