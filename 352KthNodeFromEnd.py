'''

Given a non-empty linked list and a positive integer k, return the value of k'th node from the end of the list.

Input: List = 1 —> 2 —> 3 —> 4 —> 5 —> None, k = 3
Output: 3

Assume that k is less than or equal to number of nodes in the linked list.

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data    # Data field for storing the value
        self.next = next    # Pointer to the next node

class Solution:
    def findKthNode(self, head: Node, k: int) -> int:
        # Initialize two pointers
        first = head
        second = head
        
        # Move the first pointer k steps ahead
        for _ in range(k):
            if first is None:
                return None  # In case the list is shorter than k
            first = first.next
        
        # Now move both pointers one step at a time
        while first is not None:
            first = first.next
            second = second.next
        
        # second pointer is now pointing to the k-th node from the end
        return second.data

# Helper function to print the linked list (for visualization)
def print_list(head):
    current = head
    while current:
        print(current.data, end=" —> ")
        current = current.next
    print("None")

# Example usage:
solution = Solution()

# Test case 1: List = 1 —> 2 —> 3 —> 4 —> 5 —> None, k = 3
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 3
result = solution.findKthNode(head, k)
print("K-th node from the end:", result)  # Output: 3


