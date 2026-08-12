class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    current = ListNode()
    head = current
    while list1 and list2:
        if list1.value <= list2.value:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
    head.next = list1 or list2    
        # head.next = list1 if list1 is not None else list2
    return current.next   

def print_list(list1: ListNode, list2: ListNode):
    head1 = list1
    head2 = list2
    values1 = []
    values2 = []
    while head1:
        values1.append(str(head1.value))
        head1 = head1.next
    while head2:
        values2.append(str(head2.value))
        head2 = head2.next
    print("List 1: " + " -> ".join(values1))
    print("List 2: " + " -> ".join(values2))

if __name__ == "__main__":
    # 1. Create two test lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    print("Original Lists:")
    print_list(list1, list2)
    
    # 2. Run your algorithm
    merged_list = merge_two_lists(list1, list2)
    
    print("\nMerged List:")
    current = merged_list
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    print(" -> ".join(values))