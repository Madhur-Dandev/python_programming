class Node:
	def __init__(self, val):
		self.value = val
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = self.tail = None

	def insert(self, val):
		node = Node(val)

		if self.head is None and self.tail is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def remove(self, val):
		node = self.head

		while node:
			if(node.value == val):
				if node.prev is None:
					self.head = node.next
					if self.head is not None:
						self.head.prev = None
				elif node.next is None:
					node.prev.next = None
				else:
					node.prev.next = node.next
					node.next.prev = node.prev

				break

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
