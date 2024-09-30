'''

Given a sorted list in increasing order and a single node, insert the node into its correct sorted position in the list.

Input: List = 2 —> 4 —> 6 —> 8 —> None, Node = 9
Output: 2 —> 4 —> 6 —> 8 —> 9 —> None

Input: List = 2 —> 4 —> 6 —> 8 —> None, Node = 1
Output: 1 —> 2 —> 4 —> 6 —> 8 —> None

Input: List = 1 —> 2 —> 4 —> 6 —> 8 —> 9 —> None, Node = 5
Output: 1 —> 2 —> 4 —> 5 —> 6 —> 8 —> 9 —> None

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data    # Data field for storing the value
        self.next = next    # Pointer to the next node

class Solution:
    def sortedInsert(self, head: Node, node: Node) -> Node:
        # Case 1: If the list is empty, the new node becomes the head
        if head is None:
            return node
        
        # Case 2: If the new node should be inserted before the head
        if node.data < head.data:
            node.next = head
            return node
        
        # Case 3: Traverse the list to find the correct position to insert the node
        current = head
        while current.next is not None and current.next.data < node.data:
            current = current.next
        
        # Insert the new node
        node.next = current.next
        current.next = node
        
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

# Test case 1: Inserting 9 into 2 -> 4 -> 6 -> 8 -> None
head = Node(2, Node(4, Node(6, Node(8))))
node_to_insert = Node(9)
head = solution.sortedInsert(head, node_to_insert)
print_list(head)  # Output: 2 —> 4 —> 6 —> 8 —> 9 —> None

# Test case 2: Inserting 1 into 2 -> 4 -> 6 -> 8 -> None
head = Node(2, Node(4, Node(6, Node(8))))
node_to_insert = Node(1)
head = solution.sortedInsert(head, node_to_insert)
print_list(head)  # Output: 1 —> 2 —> 4 —> 6 —> 8 —> None

# Test case 3: Inserting 5 into 1 -> 2 -> 4 -> 6 -> 8 -> 9 -> None
head = Node(1, Node(2, Node(4, Node(6, Node(8, Node(9))))))
node_to_insert = Node(5)
head = solution.sortedInsert(head, node_to_insert)
print_list(head)  # Output: 1 —> 2 —> 4 —> 5 —> 6 —> 8 —> 9 —> None

