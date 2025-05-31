class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // Create a dummy node before head to handle edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Pointer to traverse the list
        ListNode current = dummy;

        while (current.next != null) {
            if (current.next.val == val) {
                // Skip the node
                current.next = current.next.next;
            } else {
                // Move to the next node
                current = current.next;
            }
        }

        return dummy.next;
    }
}
