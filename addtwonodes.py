# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         carry=0
#         result=ListNode()
#         curr =result
#         while l1 or l2:
#             val=0
#             if l1:
#                 val +=l1.val
#             if l2:
#                 val +=l2.val
#             val +=carry
#             if val>9:
#                 carry=1
#             else:
#                 carry=0
#             newNode=ListNode(val%10)
#             curr.next=newNode
#             curr=curr.next
#             if l1:
#                 l1=l1.next
#             if l2:
#                 l2=l2.next
#         if carry:
#             newNode=ListNode(carry)
#             curr.next=newNode
#         return result.next
# sol=Solution()
# l1 = [2,4,3]
# l2 = [5,6,4]
# lis=ListNode()
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode()
        curr = result

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            newNode = ListNode(val % 10)
            curr.next = newNode
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return result.next


# Helper function to convert a list to a linked list
def to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


# Helper function to print linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))


# Test the solution
sol = Solution()
l1 = to_linked_list([2, 4, 3])
l2 = to_linked_list([5, 6, 4])


result = sol.addTwoNumbers(l1, l2)
print_linked_list(result)

