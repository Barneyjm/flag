from edge import Edge

class Emblem:
	def __init__(self, cardinals):
		assert type(cardinals) == type(())
		self.edges = {
			'north': Edge(cardinals[0]),
			'south': Edge(cardinals[1]),
			'east' : Edge(cardinals[2]),
			'west' : Edge(cardinals[3])
		}

	def __repr__(self):
		return """
		X	{0}	X
		{3}		{2}
		X	{1}	X
		""".format(self.edges['north'], 
				self.edges['south'], 
				self.edges['east'], 
				self.edges['west'])

	def set_edge(self, direction, num):
		self.edges[direction] = num

	def get_edge(self, direction):
		return self.edges[direction]

