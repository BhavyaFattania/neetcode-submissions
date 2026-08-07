# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        temp = None
        temp1 = list1
        temp2 = list2
        if temp1.val>temp2.val:
            new_head = temp1
            temp = temp1
        else:
            new_head = temp2
            temp = temp2
        print(temp.val)
        return temp