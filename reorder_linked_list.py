class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
def reorder_linked_list(head: ListNode) -> None:
    if head is None:
        return None
    # find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse the second half of the linked list
    previous = None
    current = slow.next
    slow.next = None
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node 

    # zipping the two halves together
    first = head
    second = previous
    while second:
        tem1 = first.next  # 1 -> 2 -> 3
        tem2 = second.next # 4 -> 5 -> 6
        first.next = second  # 1 -> 4
        second.next = tem1 # 4 -> 2
        first = tem1
        second = tem2