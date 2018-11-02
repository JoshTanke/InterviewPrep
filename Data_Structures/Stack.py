"""
A simple python LIFO stack class (so pretty much just a python list)

Time Complexities: O(1) for all operations

"""

class Stack:

	def __init__(self):
		self.data = []

	def push(self, val):
		self.data.append(val)

	def pop(self, val):
		if self.isEmpty():
			return None
		return self.data.pop()

	def isEmpty(self):
		return len(self.data) == 0

	def peek(self):
		if self.isEmpty():
			return None
		return self.data[-1]