from uuid import uuid4

class Node:
	def __init__(self):
		self.id = uuid4()
		self.connections = {
			'north': None,
			'south': None,
			'east': None,
			'west': None
		}

class Board:
	def __init__(self):
		self.all_nodes = {}
		self.initial_node = Node()