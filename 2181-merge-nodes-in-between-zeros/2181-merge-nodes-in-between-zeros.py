# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0)
        result_tail = None
        cur = head
        sum = 0
        while cur is not None:
            if cur.val == 0:
                if sum == 0:
                    sum = cur.val
                else:
                    if result_tail is not None:
                        result_tail.next = ListNode(sum, None)
                        result_tail = result_tail.next
                    else:
                        result_head.next = ListNode(sum, None)
                        result_tail = result_head.next
                    sum = 0
            else:
                sum += cur.val

            cur = cur.next
        return result_head.next
        