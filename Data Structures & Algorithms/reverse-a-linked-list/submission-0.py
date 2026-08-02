# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()
        if head is None:
            return head
        temp = head

        while temp.next !=None :
            stack.insert(0,temp.val)
            temp = temp.next
        head = temp
        while stack:
            temp.next = ListNode(stack.pop(0))
            temp = temp.next
        return head
        