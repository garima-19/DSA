# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.head = None 
        self.tail = None
        while list1 and list2:
            if list1.val <= list2.val:
                newnode = ListNode(list1.val)
                list1 = list1.next
            else:
                newnode = ListNode(list2.val)
                list2 = list2.next

            if self.head is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                self.tail = newnode 

        while list1:
            newnode = ListNode(list1.val)
            if self.head is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                self.tail = newnode
            list1 = list1.next

        while list2:
            newnode = ListNode(list2.val)
            if self.head is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                self.tail = newnode
            list2 = list2.next  

        return self.head
