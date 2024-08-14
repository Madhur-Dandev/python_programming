class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = self.tail = None

	def insert(self, val):
		node = Node(val)

		if self.head is None and self.tail is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def remove(self, val):
		node = prev_node = self.head

		while node:
			if(node.value == val):
				if(node == prev_node):
					self.head = self.head.next
				else:
					prev_node.next = node.next

				break

			if(node != prev_node):
				prev_node = prev_node.next
			node = node.next

	def print(self):
		node = self.head

		while node:
			print(node.value)
			node = node.next

	def delete_list(self):
		self.head = self.tail = None

ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

ll.remove(1)
ll.remove(2)
ll.remove(3)
ll.remove(4)

ll.print()

ll.delete_list()
