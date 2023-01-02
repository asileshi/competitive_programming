# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp,de = head,head
        l = 0
        ans = de
        while temp:
            l+=1
            temp = temp.next
        if l <=1:
            return None
        if l == n:
            return head.next
        i = 0
        while i+n+1<l and de:
            i+=1
            de = de.next
        de.next = de.next.next
        return ans