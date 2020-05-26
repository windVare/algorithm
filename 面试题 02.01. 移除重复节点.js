/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var removeDuplicateNodes = function(head) {
    var current = head, prev = null, arr = [];

    while (current !== null) {
        if (arr[current.val] > 0) {
            prev.next = current.next;
            current = prev.next;
        } else {
            arr[current.val] = 1;
            prev = current;
            current = prev.next;
        }
    }
    return head;
};
