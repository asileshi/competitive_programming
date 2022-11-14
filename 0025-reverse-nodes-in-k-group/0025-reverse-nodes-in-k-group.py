# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node,l,end):
            prev = None
            cur = node
            while cur:
                if l == end:
                    break
                ahead = cur.next
                cur.next = prev
                prev = cur 
                cur = ahead
                l+=1
            return [prev,cur]
        l = 0 
        s = head
        while s:
            l+=1
            s = s.next
        templist = []
        temp = ans = head
        x = 0
        while temp:
            if x+k>l:
                templist.append(temp)
                break
            mylist = reverse(temp,x,x+k)
            templist.append(mylist[0])
            temp = mylist[1]
            x+=k
        dummy = ListNode(0)
        ans = dummy
        for i in range(len(templist)):
            dummy.next = templist[i]
            while dummy.next:
                dummy = dummy.next
        return ans.next
            
            
        
        