from typing import Optional


class ListNode:
    def __init__(
        self,
        val=0,
        next=None,
    ):
        self.val = val
        self.next = next


class Solution:
    def add_values(
        self,
        first_value: int | None,
        second_value: int | None,
        previous_carry=int,
    ) -> tuple[int | None, int]:
        carry = 0
        if first_value is None or second_value is None:
            if first_value is not None:
                result = first_value
            elif second_value is not None:
                result = second_value
            result = result + previous_carry

        # first_value and second_value have value
        else:
            result = first_value + second_value + previous_carry

        if result >= 10:
            carry = 1
            result = result - 10

        return result, carry

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        # Since l1 and l2 are optional, if both are None return None
        if l1 is None or l2 is None:
            return None

        # If one of l1 or l2 is missing, return the one that isn't
        if l1 is None or l2 is None:
            head = l1 or l2
            return head

        head = ListNode()
        current_node = head
        list_iterator_1, list_iterator_2 = l1, l2
        carry = 0

        # Flag for setting the first value without adding a new node in the first iteration of the loop
        set_head = True

        # Loop continues as long as any of list_iterator_1 or list_iterator_2 is still a ListNode
        while list_iterator_1 is not None or list_iterator_2 is not None:
            value_1, value_2 = None, None
            # Get val of current node from first list and update the node iterator reference to the next node's
            if list_iterator_1 is not None:
                value_1 = list_iterator_1.val
                list_iterator_1 = list_iterator_1.next

            # Get val of current node from second list and update the node iterator reference to the next node's
            if list_iterator_2 is not None:
                value_2 = list_iterator_2.val
                list_iterator_2 = list_iterator_2.next

            result, carry = self.add_values(value_1, value_2, carry)

            # Only executed in the first iteration
            if set_head:
                head.val = result
                set_head = False
            else:
                new_node = ListNode(val=result)
                current_node.next = new_node
                current_node = current_node.next

        # If carry is left at the end of the loop, we actually need a new node
        if carry:
            new_node = ListNode(val=carry)
            current_node.next = new_node
        return head





def generate_list_nodes(vals: list[int]):
    head = None
    current = None
    for val in vals:
        if head is None:
            head = ListNode(val=val)
            current = head
        else:
            current.next = ListNode(val=val)
            current = current.next
    return head

solution = Solution()

list1 = [3,2,0,2,6,0,8,8,0,1]
list2 = [0,8,9,6,8,7,2]


l1 = generate_list_nodes(list1)
l2 = generate_list_nodes(list2)
result_1 = solution.addTwoNumbers(l1=l1, l2=l2)

