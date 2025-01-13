# Define a simple ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to print the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# Function to reverse the linked list
def linked_list_reversal(head):
    previous = None
    current = head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Create the linked list
values = [1, 2, 3, 4]
head = create_linked_list(values)
print("Original Linked List:")
print(head)

# Reverse the linked list
reversed_head = linked_list_reversal(head)
print("\nReversed Linked List:")
print(reversed_head)