'''

Given an array of integers, construct a linked list out of the array keys. The solution should create a new node for every key and efficiently insert it onto the list's tail.

Input : [1, 2, 3, 4, 5]
Output: 1 —> 2 —> 3 —> 4 —> 5 —> None

'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data    # Data field for storing the value
        self.next = next    # Pointer to the next node

class Solution:
    def construct(self, keys: List[int]) -> Node:  # Use List[int] to specify keys is a list of integers
        # Base case: if the list of keys is empty, return None
        if not keys:
            return None
        
        # Create the head of the linked list with the first key
        head = Node(keys[0])
        current = head  # This pointer will keep track of the last node (tail)
        
        # Loop through the rest of the keys and add them to the tail of the linked list
        for key in keys[1:]:
            new_node = Node(key)  # Create a new node for each key
            current.next = new_node  # Link the current node to the new node
            current = new_node  # Move the current pointer to the new node (new tail)
        
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
keys = [1, 2, 3, 4, 5]
head = solution.construct(keys)
print_list(head)
