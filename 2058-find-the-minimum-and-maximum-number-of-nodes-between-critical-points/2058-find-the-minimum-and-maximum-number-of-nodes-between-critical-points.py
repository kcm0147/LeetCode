# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        return self.findCriticalPoints(head)

    def isCriticalPoint(self, pre: ListNode, cur: ListNode, next: ListNode):
        if pre is None or next is None:
            return False
        if pre.val < cur.val and cur.val > next.val:
            return True
        if pre.val > cur.val and cur.val < next.val:
            return True
        return False

    def findCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        critical_point_ary = []
        max_distance = -1
        min_distance = (2 ** 31) - 1

        index = 1
        while cur is not None:
            next = cur.next
            next_next = next.next if next is not None else None
            if self.isCriticalPoint(cur, next, next_next):
                critical_point_ary.append(Point(index, cur.val))
                if len(critical_point_ary) >= 2:
                    cur_min_distance = critical_point_ary[-1].index - critical_point_ary[-2].index
                    cur_max_distance = critical_point_ary[-1].index - critical_point_ary[0].index
                    if cur_min_distance < min_distance:
                        min_distance = cur_min_distance
                    if cur_max_distance > max_distance:
                        max_distance = cur_max_distance
            cur = cur.next
            index = index + 1

        if len(critical_point_ary) < 2:
            return [-1, -1]
        else:
            return [min_distance, max_distance]
class Point:
    def __init__(self, index, value):
        self.index=index
        self.value=value
        