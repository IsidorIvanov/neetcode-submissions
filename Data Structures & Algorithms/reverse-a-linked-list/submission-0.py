class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        dummy = ListNode()
        curr = dummy
        for val in reversed(arr):
            curr.next = ListNode(val)  # praviš novi čvor i kačiš ga
            curr = curr.next           # pomeraš se na taj novi čvor
            
        return dummy.next