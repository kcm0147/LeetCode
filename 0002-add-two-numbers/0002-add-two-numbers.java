/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoListNode(l1,l2);
    }

    public ListNode addTwoListNode(ListNode l1, ListNode l2){
        ListNode head = new ListNode();
        ListNode answer = head;
        answer.val = 0;
        boolean isOver10 = false;
        while(true){
            ListNode next = new ListNode();
            int overValue = isOver10 ? 1: 0;
            
            if(l1.val + l2.val + overValue >= 10){
                isOver10 = true;
                answer.val = l1.val+l2.val + overValue - 10;
            }
            else{
                isOver10 = false;
                answer.val = l1.val+l2.val + overValue;
            }

        
            if(l1.next == null && l2.next == null) break;

            l1.val = 0;
            l2.val = 0;

            if(l1.next != null){
                l1 = l1.next;
            }

            if(l2.next != null){
                l2 = l2.next;
            }

            answer.next = next;
            answer = answer.next;
        }

        if(isOver10){
            ListNode next = new ListNode();
            next.val = 1;
            answer.next = next;
        }
        return head;
    }
}
    