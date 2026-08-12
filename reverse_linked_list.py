class ListNode:
	def __init__(self, value=0, next = None):
		self.value = value
		self.next = next

def reverse_Linked_list(head: ListNode) -> ListNode:
	if head is None:
		return None
	current = head
	previous = None
	while current:
		next_node = current.next
		current.next = previous
		previous = current
		current = next_node
	return previous	

def print_list(head: ListNode):
    current = head
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    print(" -> ".join(values))

if __name__ == "__main__":
    # 1. Create a longer test list: 1 -> 2 -> 3 -> 4 -> 5
    test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    print("Original List:")
    print_list(test_list)
    
    # 2. Run your algorithm
    reversed_list = reverse_Linked_list(test_list)
    
    print("\nReversed List:")
    print_list(reversed_list)	