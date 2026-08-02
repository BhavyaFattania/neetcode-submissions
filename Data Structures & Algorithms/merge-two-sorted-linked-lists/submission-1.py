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
        if temp1 is None:
            return temp2
        elif temp2 is None:
            return temp1

        if temp1.val<temp2.val:
            new_head = temp1
            temp = temp1
            temp1 = temp1.next
        else:
            new_head = temp2
            temp = temp2
            temp2= temp2.next
        while temp1 and temp2 :
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next
            else:
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
        while temp1:
            temp.next = temp1
            temp1= temp1.next
            temp = temp.next
        while temp2:
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next

        print(new_head.val)
        return new_head