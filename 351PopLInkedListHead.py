'''
Given a singly-linked list of integers, delete its head node, and advance the head pointer to point at the next node in line.

Input : 1 -> 2 —> 3 —> 4 —> None
Output: 2 —> 3 —> 4 —> None

Input : 1 —> None
Output: None

Input : None
Output: None

'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data    # Data field for storing the value
        self.next = next    # Pointer to the next node

class Solution:
    def pop(self, head: Node) -> Node:
        # If the list is empty, return None
        if head is None:
            return None
        
        # Advance the head pointer to the next node
        head = head.next
        
        # Return the new head
        return head

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" —> ")
        current = current.next
    print("None")

# Example usage:
solution = Solution()

# Test case 1: 1 -> 2 -> 3 -> 4 -> None
head = Node(1, Node(2, Node(3, Node(4))))
head = solution.pop(head)
print_list(head)  # Output: 2 —> 3 —> 4 —> None

# Test case 2: 1 -> None
head = Node(1)
head = solution.pop(head)
print_list(head)  # Output: None

# Test case 3: None
head = None
head = solution.pop(head)
print_list(head)  # Output: None

