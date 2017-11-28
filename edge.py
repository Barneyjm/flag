
class Edge:
	def __init__(self, _class):
		assert _class < 3
		self._class = _class
		self.color = set_color()

	def set_color(self):
		if self._class == 0:
			self.color = 'red'
		elif self._class == 1:
			self.color = 'blue'
		else:
			self.color = 'green'

	def get_color(self):
		return self.color