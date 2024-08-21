#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #list to temp store values
        newList = []
        #add values of linked list
        while list1 is not None:
            newList.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            newList.append(list2.val)
            list2 = list2.next
        #sort the list
        newList.sort()
        print(newList)
        #create new linked list with sorted values
        temp = ListNode(-1)
        head = temp
        for value in newList:
            temp.next = ListNode(value)
            temp = temp.next
        head = head.next
        #return linked list
        return head
