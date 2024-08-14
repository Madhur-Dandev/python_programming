head, tail = None, None

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

obj = Node(1)
head, tail = obj, obj

obj = Node(2)
tail.next = obj
tail = obj

obj = Node(3)
tail.next = obj
tail = obj

obj = Node(4)
tail.next = obj
tail = obj


print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
