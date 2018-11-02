"""
A simple python FIFO queue class using Linked List

Time Complexities: O(1) for all operations

"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return repr(self.data)	

class Queue:

	def __init__(self):
		self.head = self.tail = None
		self.count = 0

	def enQueue(self, val):
		node = Node(val)

		if not self.tail:
			self.head = node
			self.tail = self.head
		else:
			self.tail.next = node
			self.tail = node

		self.tail = node
		self.count += 1

	def deQueue(self):
		if not self.head:
			return "Empty"
		else:
			temp = self.head.data
			self.head = self.head.next
			self.count -= 1
			if not self.head: self.tail = None
			return temp


	def isEmpty(self):
		return self.count == 0

	def length(self):
		return self.count



q = Queue()
q.enQueue(1)
q.enQueue(2)
print(q.deQueue())
print(q.deQueue())
print(q.isEmpty())

q.enQueue(3)
q.enQueue(4)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())








