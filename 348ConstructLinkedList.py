'''

Given an array of integers, implement a linked list out of the array keys. The solution should create a new node for every key and insert it onto the list's front.

Input : [1, 2, 3, 4, 5]
Output: 1 —> 2 —> 3 —> 4 —> 5 —> None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, data=None, next=None):
			self.data = data	# data field
			self.next = next	# pointer to the next node
	'''

	def construct(self, keys: List[int]) -> Node:
		# Write your code here...
		if not keys:
			return None
		
		head = Node(keys[0])
		current = head     
		
		for key in keys[1:]:
			
			new_node = Node(key)
			current.next = new_node
			current = new_node
			
		return head


def print_list(head):
	current = head
	while current:
		print(current.data, end = "->")
		current = current.next
	print(None)
